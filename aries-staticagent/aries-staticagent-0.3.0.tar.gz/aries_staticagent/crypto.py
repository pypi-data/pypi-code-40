""" Crypto neccessary for packing and unpacking a message.

    Adapted from BC Gov's Indy Catalyst Agent.
    Borrowed at this point in history:
    https://github.com/bcgov/indy-catalyst/blob/14328a3eb/agent/indy_catalyst_agent/wallet/crypto.py
"""

from collections import OrderedDict
from typing import Callable, Optional, Sequence
import base64
import json

import base58
import msgpack
import pysodium

class CryptoError(Exception):
    """ CryptoError raised on failed crypto call. """


def b64_to_bytes(val: str, urlsafe=False) -> bytes:
    """Convert a base 64 string to bytes."""
    if urlsafe:
        return base64.urlsafe_b64decode(val)
    return base64.b64decode(val)


def bytes_to_b64(val: bytes, urlsafe=False) -> str:
    """Convert a byte string to base 64."""
    if urlsafe:
        return base64.urlsafe_b64encode(val).decode("ascii")
    return base64.b64encode(val).decode("ascii")


def b58_to_bytes(val: str) -> bytes:
    """Convert a base 58 string to bytes."""
    return base58.b58decode(val)


def bytes_to_b58(val: bytes) -> str:
    """Convert a byte string to base 58."""
    return base58.b58encode(val).decode("ascii")

def create_keypair(seed: bytes = None) -> (bytes, bytes):
    """
    Create a public and private signing keypair from a seed value.

    Args:
        seed: Seed for keypair

    Returns:
        A tuple of (public key, secret key)

    """
    if not seed:
        seed = random_seed()
    pk, sk = pysodium.crypto_sign_seed_keypair(seed)
    return pk, sk


def random_seed() -> bytes:
    """
    Generate a random seed value.

    Returns:
        A new random seed

    """
    return pysodium.randombytes(pysodium.crypto_secretbox_KEYBYTES)


def seed_to_did(seed: str) -> str:
    """
    Derive a did from a seed value.

    Args:
        seed: The seed to derive

    Returns:
        The did derived from the seed

    """
    seed = validate_seed(seed)
    verkey, _ = create_keypair(seed)
    did = bytes_to_b58(verkey[:16])
    return did


def validate_seed(seed: (str, bytes)) -> bytes:
    """
    Convert a seed parameter to standard format and check length.

    Args:
        seed: The seed to validate

    Returns:
        The validated and encoded seed

    """
    if not seed:
        return None
    if isinstance(seed, str):
        if "=" in seed:
            seed = b64_to_bytes(seed)
        else:
            seed = seed.encode("ascii")
    if not isinstance(seed, bytes):
        raise CryptoError("Seed value is not a string or bytes")
    if len(seed) != 32:
        raise CryptoError("Seed value must be 32 bytes in length")
    return seed


def sign_message(message: bytes, secret: bytes) -> bytes:
    """
    Sign a message using a private signing key.

    Args:
        message: The message to sign
        secret: The private signing key

    Returns:
        The signature

    """
    result = pysodium.crypto_sign(message, secret)
    sig = result[: pysodium.crypto_sign_BYTES]
    return sig


def verify_signed_message(signed: bytes, verkey: bytes) -> bool:
    """
    Verify a signed message according to a public verification key.

    Args:
        signed: The signed message
        verkey: The verkey to use in verification

    Returns:
        True if verified, else False

    """
    try:
        pysodium.crypto_sign_open(signed, verkey)
    except ValueError:
        return False
    return True


def anon_crypt_message(message: bytes, to_verkey: bytes) -> bytes:
    """
    Apply anon_crypt to a binary message.

    Args:
        message: The message to encrypt
        to_verkey: The verkey to encrypt the message for

    Returns:
        The anon encrypted message

    """
    pk = pysodium.crypto_sign_pk_to_box_pk(to_verkey)
    enc_message = pysodium.crypto_box_seal(message, pk)
    return enc_message


def anon_decrypt_message(enc_message: bytes, secret: bytes) -> bytes:
    """
    Apply anon_decrypt to a binary message.

    Args:
        enc_message: The encrypted message
        secret: The seed to use

    Returns:
        The decrypted message

    """
    sign_pk, sign_sk = create_keypair(secret)
    pk = pysodium.crypto_sign_pk_to_box_pk(sign_pk)
    sk = pysodium.crypto_sign_sk_to_box_sk(sign_sk)

    message = pysodium.crypto_box_seal_open(enc_message, pk, sk)
    return message


def auth_crypt_message(
        message: bytes, to_verkey: bytes, from_verkey: bytes, from_sigkey: bytes
) -> bytes:
    """
    Apply auth_crypt to a binary message.

    Args:
        message: The message to encrypt
        to_verkey: To recipient's verkey
        from_verkey: Sender verkey, included in combo box for verification
        from_sigkey: Sender sigkey, included to authenticated encrypt the message

    Returns:
        The encrypted message

    """
    nonce = pysodium.randombytes(pysodium.crypto_box_NONCEBYTES)
    target_pk = pysodium.crypto_sign_pk_to_box_pk(to_verkey)
    sk = pysodium.crypto_sign_sk_to_box_sk(from_sigkey)
    enc_body = pysodium.crypto_box(message, nonce, target_pk, sk)
    combo_box = OrderedDict(
        [
            ("msg", bytes_to_b64(enc_body)),
            ("sender", bytes_to_b58(from_verkey)),
            ("nonce", bytes_to_b64(nonce)),
        ]
    )
    combo_box_bin = msgpack.packb(combo_box, use_bin_type=True)
    enc_message = pysodium.crypto_box_seal(combo_box_bin, target_pk)
    return enc_message


def auth_decrypt_message(enc_message: bytes, my_verkey: bytes, my_sigkey: bytes) -> (bytes, str):
    """
    Apply auth_decrypt to a binary message.

    Args:
        enc_message: The encrypted message
        secret: Secret for signing keys

    Returns:
        A tuple of (decrypted message, sender verkey)

    """
    pk = pysodium.crypto_sign_pk_to_box_pk(my_verkey)
    sk = pysodium.crypto_sign_sk_to_box_sk(my_sigkey)
    body = pysodium.crypto_box_seal_open(enc_message, pk, sk)

    unpacked = msgpack.unpackb(body, raw=False)
    sender_vk = unpacked["sender"]
    nonce = b64_to_bytes(unpacked["nonce"])
    enc_message = b64_to_bytes(unpacked["msg"])
    sender_pk = pysodium.crypto_sign_pk_to_box_pk(b58_to_bytes(sender_vk))
    message = pysodium.crypto_box_open(enc_message, nonce, sender_pk, sk)
    return message, sender_vk


def prepare_pack_recipient_keys(
        to_verkeys: Sequence[bytes], from_verkey: bytes = None, from_sigkey: bytes = None
) -> (str, bytes):
    """
    Assemble the recipients block of a packed message.

    Args:
        to_verkeys: Verkeys of recipients
        from_verkey: Sender Verkey needed to authcrypt package
        from_sigkey: Sender Sigkey needed to authcrypt package

    Returns:
        A tuple of (json result, key)

    """
    if from_verkey is not None and from_sigkey is None or \
            from_sigkey is not None and from_verkey is None:
        raise CryptoError('Both verkey and sigkey needed to authenticated encrypt message')

    cek = pysodium.crypto_secretstream_xchacha20poly1305_keygen()
    recips = []

    for target_vk in to_verkeys:
        target_pk = pysodium.crypto_sign_pk_to_box_pk(target_vk)
        if from_verkey:
            sender_vk = bytes_to_b58(from_verkey).encode("ascii")
            enc_sender = pysodium.crypto_box_seal(sender_vk, target_pk)
            sk = pysodium.crypto_sign_sk_to_box_sk(from_sigkey)

            nonce = pysodium.randombytes(pysodium.crypto_box_NONCEBYTES)
            enc_cek = pysodium.crypto_box(cek, nonce, target_pk, sk)
        else:
            enc_sender = None
            nonce = None
            enc_cek = pysodium.crypto_box_seal(cek, target_pk)

        recips.append(
            OrderedDict(
                [
                    ("encrypted_key", bytes_to_b64(enc_cek, urlsafe=True)),
                    (
                        "header",
                        OrderedDict(
                            [
                                ("kid", bytes_to_b58(target_vk)),
                                (
                                    "sender",
                                    bytes_to_b64(enc_sender, urlsafe=True)
                                    if enc_sender
                                    else None,
                                ),
                                (
                                    "iv",
                                    bytes_to_b64(nonce, urlsafe=True)
                                    if nonce
                                    else None,
                                ),
                            ]
                        ),
                    ),
                ]
            )
        )

    data = OrderedDict(
        [
            ("enc", "xchacha20poly1305_ietf"),
            ("typ", "JWM/1.0"),
            ("alg", "Authcrypt" if from_verkey else "Anoncrypt"),
            ("recipients", recips),
        ]
    )
    return json.dumps(data), cek


def locate_pack_recipient_key(
        recipients: Sequence[dict], my_verkey: bytes, my_sigkey: bytes
) -> (bytes, str, str):
    """
    Locate pack recipient key.

    Decode the encryption key and sender verification key from a
    corresponding recipient block, if any is defined.

    Args:
        recipients: Recipients to locate
        find_key: Function used to find private key

    Returns:
        A tuple of (cek, sender_vk, recip_vk_b58)

    Raises:
        ValueError: If no corresponding recipient key found

    """
    not_found = []
    for recip in recipients:
        if not recip or "header" not in recip or "encrypted_key" not in recip:
            raise ValueError("Invalid recipient header")

        recip_vk_b58 = recip["header"].get("kid")

        if bytes_to_b58(my_verkey) != recip_vk_b58:
            not_found.append(recip_vk_b58)
            continue

        recip_vk = b58_to_bytes(recip_vk_b58)
        pk = pysodium.crypto_sign_pk_to_box_pk(my_verkey)
        sk = pysodium.crypto_sign_sk_to_box_sk(my_sigkey)

        encrypted_key = b64_to_bytes(recip["encrypted_key"], urlsafe=True)

        nonce_b64 = recip["header"].get("iv")
        nonce = b64_to_bytes(nonce_b64, urlsafe=True) if nonce_b64 else None
        sender_b64 = recip["header"].get("sender")
        enc_sender = b64_to_bytes(sender_b64, urlsafe=True) if sender_b64 else None

        if nonce and enc_sender:
            sender_vk_bin = pysodium.crypto_box_seal_open(enc_sender, pk, sk)
            sender_vk = sender_vk_bin.decode("ascii")
            sender_pk = pysodium.crypto_sign_pk_to_box_pk(b58_to_bytes(sender_vk_bin))
            cek = pysodium.crypto_box_open(encrypted_key, nonce, sender_pk, sk)
        else:
            sender_vk = None
            cek = pysodium.crypto_box_seal_open(encrypted_key, pk, sk)
        return cek, sender_vk, recip_vk_b58
    raise ValueError("No corresponding recipient key found in {}".format(not_found))


def encrypt_plaintext(
        message: str, add_data: bytes, key: bytes
) -> (bytes, bytes, bytes):
    """
    Encrypt the payload of a packed message.

    Args:
        message: Message to encrypt
        add_data:
        key: Key used for encryption

    Returns:
        A tuple of (ciphertext, nonce, tag)

    """
    nonce = pysodium.randombytes(pysodium.crypto_aead_chacha20poly1305_ietf_NPUBBYTES)
    message_bin = message.encode("ascii")
    output = pysodium.crypto_aead_chacha20poly1305_ietf_encrypt(
        message_bin, add_data, nonce, key
    )
    mlen = len(message)
    ciphertext = output[:mlen]
    tag = output[mlen:]
    return ciphertext, nonce, tag


def decrypt_plaintext(
    ciphertext: bytes, recips_bin: bytes, nonce: bytes, key: bytes
) -> str:
    """
    Decrypt the payload of a packed message.

    Args:
        ciphertext:
        recips_bin:
        nonce:
        key:

    Returns:
        The decrypted string

    """
    output = pysodium.crypto_aead_chacha20poly1305_ietf_decrypt(
        ciphertext, recips_bin, nonce, key
    )
    return output.decode("ascii")


def pack_message(
        message: str, to_verkeys: Sequence[bytes], from_verkey:bytes = None, from_sigkey: bytes = None
) -> bytes:
    """
    Assemble a packed message for a set of recipients, optionally including the sender.

    Args:
        message: The message to pack
        to_verkeys: The verkeys to pack the message for
        from_verkey: The sender verkey
        from_sigkey: The sender sigkey

    Returns:
        The encoded message

    """
    recips_json, cek = prepare_pack_recipient_keys(to_verkeys, from_verkey, from_sigkey)
    recips_b64 = bytes_to_b64(recips_json.encode("ascii"), urlsafe=True)

    ciphertext, nonce, tag = encrypt_plaintext(message, recips_b64.encode("ascii"), cek)

    data = OrderedDict(
        [
            ("protected", recips_b64),
            ("iv", bytes_to_b64(nonce, urlsafe=True)),
            ("ciphertext", bytes_to_b64(ciphertext, urlsafe=True)),
            ("tag", bytes_to_b64(tag, urlsafe=True)),
        ]
    )
    return json.dumps(data).encode("ascii")


def unpack_message(
        enc_message: bytes, my_verkey: bytes, my_sigkey: bytes
) -> (str, Optional[str], str):
    """
    Decode a packed message.

    Disassemble and unencrypt a packed message, returning the message content,
    verification key of the sender (if available), and verification key of the
    recipient.

    Args:
        enc_message: The encrypted message
        find_key: Function to retrieve private key

    Returns:
        A tuple of (message, sender_vk, recip_vk)

    Raises:
        ValueError: If the packed message is invalid
        ValueError: If the packed message reipients are invalid
        ValueError: If the pack algorithm is unsupported
        ValueError: If the sender's public key was not provided

    """
    try:
        wrapper = json.loads(enc_message)
    except Exception as err:
        raise ValueError("Invalid packed message") from err

    protected_bin = wrapper["protected"].encode("ascii")
    recips_json = b64_to_bytes(wrapper["protected"], urlsafe=True).decode("ascii")
    try:
        recips_outer = json.loads(recips_json)
    except Exception as err:
        raise ValueError("Invalid packed message recipients") from err

    alg = recips_outer["alg"]
    is_authcrypt = alg == "Authcrypt"
    if not is_authcrypt and alg != "Anoncrypt":
        raise ValueError("Unsupported pack algorithm: {}".format(alg))
    cek, sender_vk, recip_vk = locate_pack_recipient_key(
        recips_outer["recipients"], my_verkey, my_sigkey
    )
    if not sender_vk and is_authcrypt:
        raise ValueError("Sender public key not provided for Authcrypt message")

    ciphertext = b64_to_bytes(wrapper["ciphertext"], urlsafe=True)
    nonce = b64_to_bytes(wrapper["iv"], urlsafe=True)
    tag = b64_to_bytes(wrapper["tag"], urlsafe=True)

    payload_bin = ciphertext + tag
    message = decrypt_plaintext(payload_bin, protected_bin, nonce, cek)

    return message, sender_vk, recip_vk

from typing import Callable

import pytest
from web3 import Web3
from web3.contract import Contract

from raiden_contracts.constants import TEST_SETTLE_TIMEOUT_MAX, TEST_SETTLE_TIMEOUT_MIN


@pytest.fixture()
def token_network_test_storage(
    deploy_tester_contract: Callable,
    web3: Web3,
    custom_token: Web3,
    secret_registry_contract: Contract,
) -> Contract:
    return deploy_tester_contract(
        "TokenNetworkInternalStorageTest",
        [
            custom_token.address,
            secret_registry_contract.address,
            int(web3.version.network),
            TEST_SETTLE_TIMEOUT_MIN,
            TEST_SETTLE_TIMEOUT_MAX,
        ],
    )


@pytest.fixture()
def token_network_test_signatures(
    deploy_tester_contract: Contract,
    web3: Web3,
    custom_token: Contract,
    secret_registry_contract: Contract,
) -> Contract:
    return deploy_tester_contract(
        "TokenNetworkSignatureTest",
        [
            custom_token.address,
            secret_registry_contract.address,
            int(web3.version.network),
            TEST_SETTLE_TIMEOUT_MIN,
            TEST_SETTLE_TIMEOUT_MAX,
        ],
    )


@pytest.fixture()
def token_network_test_utils(
    deploy_tester_contract: Contract,
    web3: Web3,
    custom_token: Contract,
    secret_registry_contract: Contract,
) -> Contract:
    return deploy_tester_contract(
        "TokenNetworkUtilsTest",
        [
            custom_token.address,
            secret_registry_contract.address,
            int(web3.version.network),
            TEST_SETTLE_TIMEOUT_MIN,
            TEST_SETTLE_TIMEOUT_MAX,
        ],
    )

from typing import Callable, List

import pytest
from eth_typing import HexAddress
from web3 import Web3
from web3.contract import Contract, get_event_data

from raiden_contracts.constants import (
    CONTRACT_TOKEN_NETWORK,
    CONTRACT_TOKEN_NETWORK_REGISTRY,
    EVENT_TOKEN_NETWORK_CREATED,
    MAX_ETH_CHANNEL_PARTICIPANT,
    MAX_ETH_TOKEN_NETWORK,
    TEST_SETTLE_TIMEOUT_MAX,
    TEST_SETTLE_TIMEOUT_MIN,
)
from raiden_contracts.contract_manager import ContractManager
from raiden_contracts.tests.utils.constants import CONTRACT_DEPLOYER_ADDRESS

snapshot_before_token_network = None


@pytest.fixture
def get_token_network(deploy_tester_contract: Callable) -> Callable:
    """Deploy a token network as a separate contract (registry is not used)"""

    def get(arguments: List) -> Contract:
        return deploy_tester_contract(CONTRACT_TOKEN_NETWORK, arguments)

    return get


@pytest.fixture(scope="session")
def register_token_network(
    web3: Web3, token_network_registry_contract: Contract, contracts_manager: ContractManager
) -> Callable:
    """Returns a function that uses token_network_registry fixture to register
    and deploy a new token network"""

    def get(
        token_address: HexAddress,
        channel_participant_deposit_limit: int,
        token_network_deposit_limit: int,
    ) -> Contract:
        tx_hash = token_network_registry_contract.functions.createERC20TokenNetwork(
            token_address, channel_participant_deposit_limit, token_network_deposit_limit
        ).call_and_transact({"from": CONTRACT_DEPLOYER_ADDRESS})
        tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
        event_abi = contracts_manager.get_event_abi(
            CONTRACT_TOKEN_NETWORK_REGISTRY, EVENT_TOKEN_NETWORK_CREATED
        )
        event_data = get_event_data(event_abi, tx_receipt["logs"][0])
        contract_address = event_data["args"]["token_network_address"]
        contract = web3.eth.contract(
            abi=contracts_manager.get_contract_abi(CONTRACT_TOKEN_NETWORK),
            address=contract_address,
        )
        return contract

    return get


@pytest.fixture(scope="session")
def channel_participant_deposit_limit() -> int:
    return MAX_ETH_CHANNEL_PARTICIPANT


@pytest.fixture(scope="session")
def token_network_deposit_limit() -> int:
    return MAX_ETH_TOKEN_NETWORK


@pytest.fixture
def no_token_network(web3: Web3) -> None:
    """ Some tests must be executed before a token network gets created

    These tests should use this fixture. Otherwise a session level token
    network might already be registered.
    """
    if snapshot_before_token_network is not None:
        web3.testing.revert(snapshot_before_token_network)


@pytest.fixture(scope="session")
def token_network(
    register_token_network: Callable,
    custom_token: Contract,
    channel_participant_deposit_limit: int,
    token_network_deposit_limit: int,
    web3: Web3,
) -> Contract:
    """Register a new token network for a custom token"""
    global snapshot_before_token_network
    snapshot_before_token_network = web3.testing.snapshot()
    return register_token_network(
        custom_token.address, channel_participant_deposit_limit, token_network_deposit_limit
    )


@pytest.fixture
def token_network_contract(
    deploy_tester_contract: Contract,
    secret_registry_contract: Contract,
    standard_token_contract: Contract,
) -> Contract:
    network_id = int(secret_registry_contract.web3.version.network)
    return deploy_tester_contract(
        CONTRACT_TOKEN_NETWORK,
        [standard_token_contract.address, secret_registry_contract.address, network_id],
    )


@pytest.fixture()
def token_network_external(
    web3: Web3,
    get_token_network: Callable,
    custom_token: Contract,
    secret_registry_contract: Contract,
    channel_participant_deposit_limit: int,
    token_network_deposit_limit: int,
) -> Contract:
    return get_token_network(
        [
            custom_token.address,
            secret_registry_contract.address,
            int(web3.version.network),
            TEST_SETTLE_TIMEOUT_MIN,
            TEST_SETTLE_TIMEOUT_MAX,
            CONTRACT_DEPLOYER_ADDRESS,
            channel_participant_deposit_limit,
            token_network_deposit_limit,
        ]
    )

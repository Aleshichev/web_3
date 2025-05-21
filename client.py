from typing import Optional
import requests
from web3 import Web3

from utils import read_json
from data.config import TOKEN_ABI


class Client:
    default_abi = read_json(TOKEN_ABI)

    def __init__(self, private_key: str, rpc: str):
        self.private_key = private_key
        self.rpc = rpc
        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri=self.rpc))
        self.address = Web3.to_checksum_address(
            self.w3.eth.account.from_key(private_key=private_key).address
        )

    def _get_contract(self, contract_adress: str):
        return self.w3.eth.contract(
            address=Web3.to_checksum_address(contract_adress),
            abi=Client.default_abi,
        )

    def get_decimals(self, contract_adress: str) -> int:
        contract = self._get_contract(contract_adress)
        return int(contract.functions.decimals().call())

    def balance_of(self, contract_adress: str, address: Optional[str] = None):
        if not address:
            address = self.address
        contract = self._get_contract(contract_adress)
        return int(
            contract.functions.balanceOf(address).call(),
        )

    def get_allowance(self, token_address: str, spender: str):
        contract = self._get_contract(token_address)
        return int(contract.functions.allowance(self.address, spender).call())
    
    
from typing import Optional
import requests
from web3 import Web3
from models import TokenAmount
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

    def check_balance_interface(self, token_address, min_value) -> bool:
        print(f"{self.address} | balanceOf | check balance of {token_address}")
        balance = self.balance_of(contract_address=token_address)
        decimal = self.get_decimals(contract_adress=token_address)
        if balance < min_value * 10**decimal:
            print(f"{self.address} | balanceOf | not enough {token_address}")
            return False
        return True

    # ошибки data / мало газа / value слишком маленькое
    def send_transaction(self, to, data=None, from_=None, increase_gas=1.1, value=None):
        if not from_:
            from_ = self.address
        tx_params = {
            "chainId": self.w3.eth.chain_id,
            "nonce": self.w3.eth.get_transaction_count(self.address),
            "from": Web3.to_checksum_address(from_),
            "to": Web3.to_checksum_address(to),
            "gasPrice": self.w3.eth.gas_price,
        }
        if not data:
            tx_params["data"] = data
        if value:
            tx_params["value"] = value
        try:
            tx_params["gas"] = int(self.w3.eth.estimate_gas(tx_params) * increase_gas)
        except Exception as err:
            print(f"{self.address} | Transaction failed | {err}")
            return None

        sign = self.w3.eth.account.sign_transaction(tx_params, self.private_key)
        return self.w3.eth.send_raw_transaction(sign.rawTransaction)

    def verif_tx(self, tx_hash) -> bool:
        try:
            data = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=200)
            if "status" in data and data["status"] == 1:
                print(f"{self.address} | transaction was successful: {tx_hash.hex()}")
                return True
            else:
                print(
                    f'{self.address} | transaction failed: {data["transactionHash"].hex()}'
                )
                return False
        except Exception as err:
            print(f"{self.address} |unexpected error in <verif_tx> function: {err}")
            return False

    def approve(self, token_address, spender, amount: Optional[TokenAmount] = None):
        contract = self._get_contract(token_address)
        return self.send_transaction(
            to=token_address,
            data=contract.encodeABI("approve", args=(spender, amount.Wei)),
        )

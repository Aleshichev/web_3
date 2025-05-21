# from web3.middleware import geth_poa_middleware
from typing import Optional
import json

# def get_private_from_seed(seed: str) -> str:
#     web3 = Web3(Web3.HTTPProvider(endpoint_uri=arb_rpc))
#     web3.middleware_onion.inject(geth_poa_middleware, layer=0)
#     web3.eth.account.enable_unaudited_hdwallet_features()
#     web3_account: LocalAccount = web3.eth.account.from_mnemonic(seed)
#     private_key = web3_account._private_key.hex()
#     return private_key


def read_json(path: str, encoding: Optional[str] = None) -> list | dict:
    return json.load(open(path, encoding=encoding))
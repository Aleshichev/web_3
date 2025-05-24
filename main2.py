from client import Client
from data.config import private_key, arb_rpc, usdc_arb
from time import sleep
from tasks.woofi import WooFi
from models import Arbitrum, Avalanche
from web3.middleware import ExtraDataToPOAMiddleware


client = Client(private_key=private_key, network=Arbitrum)
client.w3.middleware_onion.inject(ExtraDataToPOAMiddleware(), layer=0)
block = client.w3.eth.get_block("latest")

# print(client.get_decimals(contract_address="0xaf88d065e77c8cC2239327C5EDb3A432268e5831"))
# sleep(5)
# print(client.balance_of(contract_address=usdc_arb))
# print(client.w3.eth.get_block("latest"))
# print(client.w3.eth.max_priority_fee)
# woofi = WooFi(client=client)
# amount=TokenAmount(amount=0.0005)
# tx = woofi.swap_eth_to_usdc(amount=amount)
# tx = woofi.swap_usdc_to_eth()
# res = woofi.client.verif_tx(tx_hash=tx)

# print(res)
res = Client.get_max_priority_fee_per_gas(w3=client.w3, block=block)
print(res)
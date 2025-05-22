from client import Client
from data.config import private_key, arb_rpc, usdc_arb
from time import sleep
from tasks.woofi import WooFi
from models import TokenAmount

client = Client(private_key=private_key, rpc=arb_rpc)
# print(client.get_decimals(contract_address="0xaf88d065e77c8cC2239327C5EDb3A432268e5831"))
# sleep(5)
# print(client.balance_of(contract_address=usdc_arb))


woofi = WooFi(client=client)
# amount=TokenAmount(amount=0.0005)
# tx = woofi.swap_eth_to_usdc(amount=amount)
tx = woofi.swap_usdc_to_eth()
# res = woofi.client.verif_tx(tx_hash=tx)

# print(res)
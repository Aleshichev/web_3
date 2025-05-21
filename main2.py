from client import Client
from data.config import private_key, arb_rpc, usdc_arb
from time import sleep

client = Client(private_key=private_key, rpc=arb_rpc)
# print(client.get_decimals(contract_adress="0xaf88d065e77c8cC2239327C5EDb3A432268e5831"))
# sleep(5)
# print(client.balance_of(contract_adress=usdc_arb))

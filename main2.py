from client import Client
from data.config import private_key, arb_rpc


client = Client(private_key=private_key, rpc=arb_rpc)
print(client.get_decimals(contract_adress="0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"))

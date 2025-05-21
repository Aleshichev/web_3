from web3 import Web3
from data.config import arb_rpc, bsc_rpc, private_key
from eth_account.signers.local import LocalAccount
#from utils import get_private_from_seed



web3 = Web3(Web3.HTTPProvider(endpoint_uri=arb_rpc))
print(f"is connected: {web3.is_connected()}")

# получение параметров блокчейна
# print(f"gas price: {web3.eth.gas_price} wei")
# print(f"current block number: {web3.eth.block_number}")
# print(f"number of current chain is {web3.eth.chain_id}")

# balance / 10 ** 18 - перевести из wei to ETH значение  DECIMAL = 18
# проверка баланса в нативной монете
account = web3.eth.account.from_key(private_key=private_key)
wallet_address = account.address
balance = web3.eth.get_balance(wallet_address)
print(f"balance of {wallet_address} is {balance } ")

# перевести баланс в eth, gwei, wei
ether_balance = web3.from_wei(balance, "ether")
print(f"balance of {wallet_address} is {ether_balance} ETH")
print(f"balance of {wallet_address} is {web3.from_wei(balance, 'gwei')} GWEI")
print(f"balance of {wallet_address} is {web3.to_wei(ether_balance, 'ether')} WEI")



# получение приватного ключа из сид фразы
# private_key = get_private_from_seed(seed=seed)
# print(private_key)


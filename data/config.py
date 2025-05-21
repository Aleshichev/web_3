import os
import sys
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()  # загружает переменные из .env

arb_rpc = os.getenv('ARB_RPC')
bsc_rpc = os.getenv('BSC_RPC')
private_key = os.getenv('PRIVATE_KEY')

if getattr(sys, "frozen", False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, "abis")
TOKEN_ABI = os.path.join(ABIS_DIR, "token.json")
WOOFI_ABI = os.path.join(ABIS_DIR, "woofi.json")


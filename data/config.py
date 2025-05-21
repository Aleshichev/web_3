import os
import sys
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

arb_rpc = 'https://arb-pokt.nodies.app'
bsc_rpc = 'https://bsc-rpc.publicnode.com'
private_key = os.getenv('PRIVATE_KEY')
usdc_arb = "0xaf88d065e77c8cC2239327C5EDb3A432268e5831"

if getattr(sys, "frozen", False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, "abis")
TOKEN_ABI = os.path.join(ABIS_DIR, "token.json")
WOOFI_ABI = os.path.join(ABIS_DIR, "woofi.json")


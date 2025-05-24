from dataclasses import dataclass
from decimal import Decimal
from typing import Union


# class TokenAmount:
#     Wei: int
#     Ether: Decimal
#     decimals: int

#     def __init__(
#         self,
#         amount: Union[int, float, str, Decimal],
#         decimals: int = 18,
#         wei: bool = False,
#     ) -> None:
#         if wei:
#             # print(f"amount = {amount!r}")
#             self.Wei: int = amount
#             self.Ether: Decimal = Decimal(str(amount)) / 10**decimals
#         else:
#             self.Wei: int = int(Decimal(str(amount)) * 10**decimals)
#             self.Ether: Decimal = Decimal(str(amount))

#         self.decimals = decimals
from decimal import Decimal, InvalidOperation
from typing import Union

class TokenAmount:
    Wei: int
    Ether: Decimal
    decimals: int

    def __init__(
        self,
        amount: Union[int, float, str, Decimal],
        decimals: int = 18,
        wei: bool = False,
    ) -> None:
        self.decimals = decimals

        try:
            # Преобразуем amount в Decimal максимально корректно
            if isinstance(amount, Decimal):
                dec_amount = amount
            elif isinstance(amount, (int, float)):
                dec_amount = Decimal(str(amount))
            elif isinstance(amount, str):
                dec_amount = Decimal(amount.strip())
            else:
                raise TypeError(f"Unsupported amount type: {type(amount)}")

        except (InvalidOperation, TypeError) as e:
            raise ValueError(f"Invalid amount for Decimal conversion: {amount!r}") from e

        if wei:
            # amount уже в Wei, сохраняем как int
            if not isinstance(amount, int):
                # Если не int, пытаемся преобразовать в int
                try:
                    self.Wei = int(dec_amount)
                except Exception as e:
                    raise ValueError(f"Cannot convert wei amount to int: {amount!r}") from e
            else:
                self.Wei = amount

            self.Ether = dec_amount / Decimal(10 ** decimals)
        else:
            # amount — это Ether, нужно получить Wei
            self.Ether = dec_amount
            self.Wei = int((dec_amount * Decimal(10 ** decimals)).to_integral_value())



class Network:
    def __init__(
        self,
        name: str,
        rpc: str,
        chain_id: int,
        eip1559_tx: bool,
        coin_symbol: str,
        explorer: str,
        decimals: int = 18,
    ):
        self.name = name
        self.rpc = rpc
        self.chain_id = chain_id
        self.eip1559_tx = eip1559_tx
        self.coin_symbol = coin_symbol
        self.decimals = decimals
        self.explorer = explorer

    def __str__(self):
        return f"{self.name}"


Arbitrum = Network(
    name="arbitrum",
    #rpc="https://arb-pokt.nodies.app",
    rpc="https://arbitrum.meowrpc.com",
    chain_id=42161,
    eip1559_tx=True,
    coin_symbol="ETH",
    explorer="https://arbiscan.io/",
)


Optimism = Network(
    name="optimism",
    rpc="https://rpc.ankr.com/optimism/",
    chain_id=10,
    eip1559_tx=True,
    coin_symbol="ETH",
    explorer="https://optimistic.etherscan.io/",
)


Polygon = Network(
    name="polygon",
    rpc="https://polygon-rpc.com/",
    chain_id=137,
    eip1559_tx=True,
    coin_symbol="MATIC",
    explorer="https://polygonscan.com/",
)


Avalanche = Network(
    name="avalanche",
    rpc="https://avalanche-c-chain-rpc.publicnode.com",
    chain_id=43114,
    eip1559_tx=True,
    coin_symbol="AVAX",
    explorer="https://snowtrace.io/",
)


Fantom = Network(
    name="fantom",
    rpc="https://rpc.ankr.com/fantom/",
    chain_id=250,
    eip1559_tx=True,
    coin_symbol="FTM",
    explorer="https://ftmscan.com/",
)

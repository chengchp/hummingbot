from hummingbot.connector.derivative.grvt_perpetual import grvt_perpetual_constants as CONSTANTS


def combine_to_hb_trading_pair(base: str, quote: str) -> str:
    """
    Combine base and quote to Hummingbot trading pair format
    """
    return f"{base}-{quote}"


def split_hb_trading_pair(trading_pair: str) -> tuple[str, str]:
    """
    Split Hummingbot trading pair to base and quote
    """
    return trading_pair.split("-")


def convert_from_exchange_symbol(symbol: str) -> str:
    """
    Convert exchange symbol to Hummingbot trading pair
    """
    # Placeholder - need to implement based on actual GRVT symbol format
    return symbol


def convert_to_exchange_symbol(trading_pair: str) -> str:
    """
    Convert Hummingbot trading pair to exchange symbol
    """
    # Placeholder - need to implement based on actual GRVT symbol format
    return trading_pair.replace("-", "")

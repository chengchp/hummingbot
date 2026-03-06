"""
GRVT Perpetual Constants
GRVT (Gravity Markets) Exchange
"""

from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit
from hummingbot.core.data_type.in_flight_order import OrderState

EXCHANGE_NAME = "grvt_perpetual"
DEFAULT_DOMAIN = "grvt_perpetual"
BROKER_ID = "HBOT"

MAX_ORDER_ID_LEN = 32

PERPETUAL_INSTRUMENT_TYPE = "PERPETUAL"

# GRVT API Environments
# Production
EDGE_PROD = "https://edge.grvt.io"
WSS_PROD = "wss://trades.grvt.io/ws/full"

# Testnet
EDGE_TESTNET = "https://edge.testnet.grvt.io"
WSS_TESTNET = "wss://trades.testnet.grvt.io/ws/full"

# Dev
EDGE_DEV = "https://edge.dev.gravitymarkets.io"
WSS_DEV = "wss://trades.dev.gravitymarkets.io/ws/full"

# Staging
EDGE_STAGING = "https://edge.staging.gravitymarkets.io"
WSS_STAGING = "wss://trades.staging.gravitymarkets.io/ws/full"

# Chain IDs
CHAIN_ID_MAINNET = 325
CHAIN_ID_TESTNET = 326

# REST API Base URLs
BASE_URLS = {
    "prod": EDGE_PROD,
    "testnet": EDGE_TESTNET,
    "dev": EDGE_DEV,
    "staging": EDGE_STAGING,
}

WSS_URLS = {
    "prod": WSS_PROD,
    "testnet": WSS_TESTNET,
    "dev": WSS_DEV,
    "staging": WSS_STAGING,
}

# Default domain
DEFAULT_DOMAIN = "testnet"

# REST API Endpoints - Auth
AUTH_API_KEY_LOGIN = "/auth/api_key/login"
AUTH_WALLET_LOGIN = "/auth/wallet/login"

# REST API Endpoints - Market Data
MARKET_INSTRUMENTS = "/v1/market/instruments"
MARKET_TICKERS = "/v1/market/tickers"
MARKET_ORDERBOOK = "/v1/market/orderbook"
MARKET_KLINES = "/v1/market/klines"
MARKET_FUNDING = "/v1/market/funding"

# REST API Endpoints - Trading
TRADE_ORDER_CREATE = "/v1/trade/order/create"
TRADE_ORDER_CANCEL = "/v1/trade/order/cancel"
TRADE_ORDER_CANCEL_ALL = "/v1/trade/order/cancel/all"
TRADE_ORDER_GET = "/v1/trade/order/get"
TRADE_ORDER_LIST = "/v1/trade/order/list"
TRADE_ORDER_HISTORY = "/v1/trade/order/history"

# REST API Endpoints - Account
ACCOUNT_BALANCE = "/v1/account/balance"
ACCOUNT_POSITIONS = "/v1/account/positions"
ACCOUNT_POSITION_HISTORY = "/v1/account/positions/history"
ACCOUNT_FUNDING = "/v1/account/funding"
ACCOUNT_WALLET_HISTORY = "/v1/account/wallet/history"

# WebSocket Channels
WS_CHANNEL_ORDERBOOK = "v1.book"
WS_CHANNEL_TRADE = "v1.trades"
WS_CHANNEL_TICKER = "v1.ticker"
WS_CHANNEL_POSITION = "v1.account.positions"
WS_CHANNEL_ORDER = "v1.account.orders"

# Order States
ORDER_STATE_MAP = {
    "pending": OrderState.OPEN,
    "open": OrderState.OPEN,
    "filled": OrderState.FILLED,
    "partial": OrderState.PARTIALLY_FILLED,
    "cancelled": OrderState.CANCELED,
    "rejected": OrderState.FAILED,
}

# Rate Limits (placeholder - need to confirm from GRVT)
GET_RATE = 10  # per second
POST_RATE = 10  # per second

RATE_LIMITS = [
    RateLimit(limit_id="public", limit=GET_RATE, time_interval=1),
    RateLimit(limit_id="private", limit=POST_RATE, time_interval=1),
]

# WebSocket Heartbeat
WS_HEARTBEAT_TIME_INTERVAL = 30.0

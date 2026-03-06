from hummingbot.core.data_type.common import OrderType, PositionMode
from hummingbot.core.data_type.in_flight_order import OrderState

EXCHANGE_NAME = "grvt_perpetual"

DEFAULT_DOMAIN = "grvt_perpetual_main"

DEFAULT_TIME_IN_FORCE = "GTC"

# GRVT API URLs (to be confirmed from official docs)
REST_URLS = {
    "grvt_perpetual_main": "https://api.grvt.io/",
    "grvt_perpetual_testnet": "https://api.testnet.grvt.io/"
}

WSS_PUBLIC_URLS = {
    "grvt_perpetual_main": "wss://stream.grvt.io/ws/",
    "grvt_perpetual_testnet": "wss://stream.testnet.grvt.io/ws/"
}

WSS_PRIVATE_URLS = {
    "grvt_perpetual_main": "wss://stream.grvt.io/ws/",
    "grvt_perpetual_testnet": "wss://stream.testnet.grvt.io/ws/"
}

WS_HEARTBEAT_TIME_INTERVAL = 20.0

# API Key and signature related
X_API_RECV_WINDOW = str(50000)

HBOT_BROKER_ID = "Hummingbot"

MAX_ID_LEN = 36
SECONDS_TO_WAIT_TO_RECEIVE_MESSAGE = 30

ORDER_TYPE_MAP = {
    OrderType.LIMIT: "Limit",
    OrderType.MARKET: "Market",
}

POSITION_MODE_API_ONEWAY = "oneway"
POSITION_MODE_API_HEDGE = "hedge"

POSITION_MODE_MAP = {
    PositionMode.ONEWAY: POSITION_MODE_API_ONEWAY,
    PositionMode.HEDGE: POSITION_MODE_API_HEDGE,
}

# REST API Endpoints (placeholder - need to confirm from GRVT API docs)
LATEST_SYMBOL_INFORMATION_ENDPOINT = "v1/market/tickers"
QUERY_SYMBOL_ENDPOINT = "v1/market/instruments"
ORDER_BOOK_ENDPOINT = "v1/market/orderbook"
SERVER_TIME_PATH_URL = "v1/common/time"

# REST API Private Endpoints
SET_LEVERAGE_PATH_URL = "v1/position/leverage"
GET_POSITIONS_PATH_URL = "v1/position/list"
PLACE_ACTIVE_ORDER_PATH_URL = "v1/order/create"
CANCEL_ACTIVE_ORDER_PATH_URL = "v1/order/cancel"
QUERY_ACTIVE_ORDER_PATH_URL = "v1/order/query"
USER_TRADE_RECORDS_PATH_URL = "v1/execution/list"
GET_WALLET_BALANCE_PATH_URL = "v1/account/balance"
SET_POSITION_MODE_URL = "v1/position/mode"

# WebSocket Public Endpoints
WS_PING_REQUEST = "ping"
WS_TRADES_TOPIC = "trade"
WS_ORDER_BOOK_EVENTS_TOPIC = "orderbook"
WS_INSTRUMENTS_INFO_TOPIC = "tickers"

# WebSocket Private Endpoints
WS_AUTHENTICATE_USER_ENDPOINT_NAME = "auth"
WS_SUBSCRIPTION_POSITIONS_ENDPOINT_NAME = "position"
WS_SUBSCRIPTION_ORDERS_ENDPOINT_NAME = "order"
WS_SUBSCRIPTION_EXECUTIONS_ENDPOINT_NAME = "execution"
WS_SUBSCRIPTION_WALLET_ENDPOINT_NAME = "wallet"

# Order Statuses (placeholder - need to confirm)
ORDER_STATE = {
    "Created": OrderState.OPEN,
    "New": OrderState.OPEN,
    "Filled": OrderState.FILLED,
    "PartiallyFilled": OrderState.PARTIALLY_FILLED,
    "Cancelled": OrderState.CANCELED,
    "PendingCancel": OrderState.PENDING_CANCEL,
    "Rejected": OrderState.FAILED,
}

GET_LIMIT_ID = "GETLimit"
POST_LIMIT_ID = "POSTLimit"
GET_RATE = 49  # per second
POST_RATE = 19  # per second

# Request error codes (placeholder)
RET_CODE_OK = 0

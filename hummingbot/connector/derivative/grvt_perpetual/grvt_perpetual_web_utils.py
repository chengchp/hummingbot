from hummingbot.connector.derivative.grvt_perpetual.grvt_perpetual_auth import GRVTPerpetualAuth
from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit
from hummingbot.core.web_assistant.connections.data_types import RESTMethod, RESTAssistant
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory

from hummingbot.connector.derivative.grvt_perpetual import grvt_perpetual_constants as CONSTANTS


def build_api_factory(authenticator: GRVTPerpetualAuth) -> WebAssistantsFactory:
    """
    Build API factory for GRVT
    """
    return WebAssistantsFactory(
        throttler=None,  # Will be set by connector
        auth=authenticator,
    )


def build_rate_limits(trading_pairs=None) -> list[RateLimit]:
    """
    Build rate limits for GRVT API
    """
    return [
        RateLimit(
            limit_id=CONSTANTS.GET_LIMIT_ID,
            linked_limit_weights=[LinkedLimitWeightPair(CONSTANTS.GET_RATE)],
            limit=CONSTANTS.GET_RATE,
            time_interval=1
        ),
        RateLimit(
            limit_id=CONSTANTS.POST_LIMIT_ID,
            linked_limit_weights=[LinkedLimitWeightPair(CONSTANTS.POST_RATE)],
            limit=CONSTANTS.POST_RATE,
            time_interval=1
        ),
    ]


def public_rest_url(path_url: str, domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Generate public REST API URL
    """
    return CONSTANTS.REST_URLS.get(domain, CONSTANTS.REST_URLS[CONSTANTS.DEFAULT_DOMAIN]) + path_url


def private_rest_url(path_url: str, domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Generate private REST API URL
    """
    return CONSTANTS.REST_URLS.get(domain, CONSTANTS.REST_URLS[CONSTANTS.DEFAULT_DOMAIN]) + path_url


def public_ws_url(domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Generate public WebSocket URL
    """
    return CONSTANTS.WSS_PUBLIC_URLS.get(domain, CONSTANTS.WSS_PUBLIC_URLS[CONSTANTS.DEFAULT_DOMAIN])


def private_ws_url(domain: str = CONSTANTS.DEFAULT_DOMAIN) -> str:
    """
    Generate private WebSocket URL
    """
    return CONSTANTS.WSS_PRIVATE_URLS.get(domain, CONSTANTS.WSS_PRIVATE_URLS[CONSTANTS.DEFAULT_DOMAIN])

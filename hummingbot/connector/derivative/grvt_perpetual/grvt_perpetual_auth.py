import hashlib
import hmac
import time
from typing import Dict

from hummingbot.connector.derivative.grvt_perpetual import grvt_perpetual_constants as CONSTANTS
from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory


class GRVTPerpetualAuth:
    """
    Auth class for GRVT API authentication
    """

    def __init__(self, api_key: str, secret_key: str, time_synchronizer):
        self.api_key = api_key
        self.secret_key = secret_key
        self._time_synchronizer = time_synchronizer

    async def rest_authenticate(self, request: any) -> any:
        """
        Adds authentication to a REST API request
        """
        timestamp = str(int(time.time() * 1000))
        signature = self._generate_signature(timestamp, request)
        
        request.headers["X-BAPI-API-KEY"] = self.api_key
        request.headers["X-BAPI-SIGN"] = signature
        request.headers["X-BAPI-SIGN-TYPE"] = "2"
        request.headers["X-BAPI-TIMESTAMP"] = timestamp
        request.headers["X-BAPI-RECV-WINDOW"] = CONSTANTS.X_API_RECV_WINDOW
        
        return request

    def _generate_signature(self, timestamp: str, request: any) -> str:
        """
        Generate signature for API request
        """
        # This is a placeholder - need to implement based on actual GRVT API specs
        # Typically involves: HMAC-SHA256(timestamp + method + path + body)
        param_str = ""
        if hasattr(request, 'params') and request.params:
            param_str = "&".join([f"{k}={v}" for k, v in request.params.items()])
        
        message = timestamp + request.method + request.url.path + param_str
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
        return signature

    async def ws_authenticate(self, ws_connection: any) -> Dict[str, any]:
        """
        Authenticate WebSocket connection
        """
        timestamp = str(int(time.time() * 1000))
        signature = self._generate_ws_signature(timestamp)
        
        auth_message = {
            "op": "auth",
            "args": [self.api_key, timestamp, signature]
        }
        
        return auth_message

    def _generate_ws_signature(self, timestamp: str) -> str:
        """
        Generate signature for WebSocket authentication
        """
        message = timestamp + "ws"
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
        return signature

    def get_rate_limits(self) -> list[RateLimit]:
        """
        Get rate limits for API requests
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

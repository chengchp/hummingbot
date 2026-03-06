"""
GRVT Perpetual Auth
GRVT uses session cookie authentication via API Key login
"""

import aiohttp
from typing import Dict, Optional

from hummingbot.connector.derivative.grvt_perpetual import grvt_perpetual_constants as CONSTANTS
from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory


class GRVTPerpetualAuth:
    """
    Auth class for GRVT API authentication
    GRVT uses session cookie authentication - not traditional HMAC signatures
    """

    def __init__(
        self,
        api_key: str,
        secret_key: Optional[str] = None,
        sub_account_id: Optional[str] = None,
        domain: str = CONSTANTS.DEFAULT_DOMAIN,
    ):
        self.api_key = api_key
        self.secret_key = secret_key or api_key  # For GRVT, API key is the secret
        self.sub_account_id = sub_account_id
        self._domain = domain
        self._session_cookie: Optional[str] = None
        self._account_id: Optional[str] = None

    @property
    def base_url(self) -> str:
        return CONSTANTS.BASE_URLS.get(self._domain, CONSTANTS.BASE_URLS[CONSTANTS.DEFAULT_DOMAIN])

    @property
    def ws_url(self) -> str:
        return CONSTANTS.WSS_URLS.get(self._domain, CONSTANTS.WSS_URLS[CONSTANTS.DEFAULT_DOMAIN])

    async def authenticate(self, api_factory: WebAssistantsFactory) -> Dict[str, str]:
        """
        Authenticate via API Key and get session cookie
        """
        if self._session_cookie and self._account_id:
            return {
                "Cookie": self._session_cookie,
                "X-Grvt-Account-Id": self._account_id,
            }

        auth_url = f"{self.base_url}{CONSTANTS.AUTH_API_KEY_LOGIN}"

        payload = {"api_key": self.api_key}
        if self.sub_account_id:
            payload["sub_account_id"] = self.sub_account_id

        # Make authentication request
        # Note: This is a simplified version - actual implementation needs to handle the response
        # to extract the session cookie and account ID
        
        headers = {
            "Content-Type": "application/json",
            "Cookie": "rm=true;",
        }

        return headers

    async def get_auth_headers(self) -> Dict[str, str]:
        """
        Get authentication headers for requests
        """
        headers = {}
        if self._session_cookie:
            headers["Cookie"] = self._session_cookie
        if self._account_id:
            headers["X-Grvt-Account-Id"] = self._account_id
        return headers

    async def ws_auth_message(self) -> Dict[str, any]:
        """
        Get WebSocket authentication message
        """
        return {
            "op": "auth",
            "data": {
                "api_key": self.api_key,
            }
        }

    def get_rate_limits(self) -> list[RateLimit]:
        return CONSTANTS.RATE_LIMITS

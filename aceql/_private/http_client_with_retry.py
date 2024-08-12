import time
import requests
from requests.exceptions import RequestException, Timeout


class HTTPClientWithRetry:
    MAX_RETRIES = 0
    RETRY_INTERVAL_MS = 0

    @staticmethod
    def set_max_retries(max_retries):
        """Sets the maximum number of retries."""
        HTTPClientWithRetry.MAX_RETRIES = max_retries

    @staticmethod
    def set_retry_interval_ms(retry_interval_ms):
        """Sets the retry interval in milliseconds."""
        HTTPClientWithRetry.RETRY_INTERVAL_MS = retry_interval_ms

    @staticmethod
    def get(url, **kwargs):
        attempt = 0
        while True:
            try:
                response = requests.get(url, **kwargs)
                response.raise_for_status()  # Raise an exception for HTTP error codes
                return response
            except (RequestException, Timeout) as e:
                attempt += 1
                if attempt > HTTPClientWithRetry.MAX_RETRIES:
                    raise e
                time.sleep(HTTPClientWithRetry.RETRY_INTERVAL_MS / 1000.0)  # Convert ms to seconds

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        attempt = 0
        while True:
            try:
                response = requests.post(url, data=data, json=json, **kwargs)
                response.raise_for_status()  # Raise an exception for HTTP error codes
                return response
            except (RequestException, Timeout) as e:
                attempt += 1
                if attempt > HTTPClientWithRetry.MAX_RETRIES:
                    raise e
                time.sleep(HTTPClientWithRetry.RETRY_INTERVAL_MS / 1000.0)  # Convert ms to seconds

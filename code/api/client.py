import logging
import socket
from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


logger = logging.getLogger('pytest')


class ApiClient:

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def _request(self, location, method=None, expected_status=None, headers=None, data=None, cookies=None,
                 allow_redirects=True):
        if expected_status is None:
            expected_status = 200

        url = urljoin(self.url, location)

        self._log_pre_request(method, url, headers, data, cookies, expected_status, allow_redirects)
        response = self.session.request(method=method, url=url, headers=headers, data=data, cookies=cookies,
                                        allow_redirects=allow_redirects)
        self._log_post_request(url, response)

        assert response.status_code == expected_status, \
            ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"! '
                                        f'Expected status code {expected_status}.')

        return response

    def register(self, credentials):
        headers = {
            'Host': 'localhost:8080',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'name': '',
            'username': credentials['username'],
            'password': credentials['password']
        }

        return self._request(location='signup', method='POST', headers=headers, data=data)

    def login(self, credentials):
        headers = {
            'Host': 'localhost:8080',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'username': credentials['username'],
            'password': credentials['password']
        }

        return self._request(location='login', method='POST', expected_status=302, headers=headers, data=data,
                             allow_redirects=False)

    @staticmethod
    def _log_post_request(url, response):
        logger.info(f'Response from {url}\n'
                    f'\tcode: {response.status_code}\n'
                    f'\theaders: {response.headers}\n'
                    f'\tcookies: {response.cookies}\n'
                    f'\ttext: {response.text}\n\n')

    @staticmethod
    def _log_pre_request(method, url, headers, data, cookies, expected_status, allow_redirects):
        ip = socket.gethostbyname(socket.gethostname())
        logger.info(f'{ip} -- {method} request for {url}\n'
                    f'\tExpected status code = {expected_status}, allow redirects = {allow_redirects}\n'
                    f'\theaders = {headers}\n'
                    f'\tdata = {data}\n'
                    f'\tcookies = {cookies}\n')

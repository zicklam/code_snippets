#!/usr/bin/env python3

"""
------__--------------------------------------------------------------------
 ____/ _|
|_  / |_   author   : F. Zicklam
 / /|  _|  editor   : F. Zicklam
/___|_|    last edit: 2021-08-11
----------------------------------------------------------------------------

Simple Http class to send json API requests
Supports:
    - GET, POST, PUT, DELETE
    - POST + PUT with Content-Type Header (application/json)
    - PUT with ETag if provided

Example usage after import:

    # Create instance:
    self._http = Http(url, user, secret)

    # Http call:
    response, code, *_ = self._http('PUT', '/object/endpoint', etag=self_etag, data=json.dumps(data))

    # Http call with more output
    response, code, headers, content = self._http('GET', '/object/endpoint')
    etag = headers['ETag'][1:-1]
"""

import requests

class Http():
    def __init__(self, url=None, user=None, secret=None, **kwargs):
        """ HTTP Configuration """
        self._timeout = 30.0

        self._user   = user
        self._secret = secret
        self._url    = url

        """ build up http session """
        self._session = requests.session()
        self._session.headers['Authorization'] = f"Bearer {self._user} {self._secret}"
        self._session.headers['Accept'] = 'application/json'

    """ Generic method (__call__ method enable instance like function behavior) """
    def __call__(self, method, uri, **kwargs):
        url = f"{self._url}/{uri}"

        if method.casefold() in map(str.casefold, ['post','put']):
            self._session.headers['Content-Type'] = 'application/json'

        if method.casefold() in map(str.casefold, ['put']) and kwargs['etag']:
            self._session.headers['If-Match'] = kwargs.pop('etag')

        headers = self._session.headers

        try:
            response = requests.request(method=method, url=url, headers=headers, **kwargs, timeout=self._timeout)
            response.raise_for_status()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as errc:
            print("Error C: " + errc)
            return response.ok, response.status_code, response.headers, response.text
        except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as errh:
            print("Error H: " + errh)
            return response.ok, response.status_code, response.headers, response.text
        finally:
            return response.ok, response.status_code, response.headers, response.text

# vim: set ts=4 sw=4 sts=4 tw=0 et :

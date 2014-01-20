import hashlib

from django.test.client import Client
from django_nose.testcases import FastFixtureTestCase

CONTENT_TYPE = 'application/x-www-form-urlencoded'


class ApiClient(object):
    def __init__(self, api_key, api_secret, auth_key=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.auth_key = auth_key
        self.client = Client()

    def _update_params(self, url_path, params, data):
        params.update({"api_key": self.api_key})
        if self.auth_key:
            params.update({"auth_key": self.auth_key})

        # get data from request
        data = {k: v for k, v in data.items()}
        data.update({k: v for k, v in params.items()})

        # generate signature
        sorted_keys = sorted(data.keys())
        message = "%s%s%s" % (url_path,
                "".join("%s=%s" % (k, data[k]) for k in sorted_keys),
                self.api_secret)
        sha = hashlib.sha1()
        sha.update(message)
        api_sig = sha.hexdigest()
        params.update({"api_sig": api_sig})

    def get(self, url_path, params=None, **kwargs):
        if not params:
            params = {}
        self._update_params(url_path, params, {})
        return self.client.get(url_path, params, **kwargs)

    def post(self, url_path, params=None, data=None, **kwargs):
        if not params:
            params = {}
        if not data:
            data = {}
        self._update_params(url_path, params, data)
        url = "%s?%s" % (url_path, "&".join("%s=%s" % (k, v) for k, v in params.items()))
        body = "&".join("%s=%s" % (k, v) for k, v in data.items())
        return self.client.post(url, data=body, content_type=CONTENT_TYPE, **kwargs)

    def put(self, url_path, params=None, data=None, **kwargs):
        if not params:
            params = {}
        if not data:
            data = {}
        self._update_params(url_path, params, data)
        url = "%s?%s" % (url_path, "&".join("%s=%s" % (k, v) for k, v in params.items()))

        body = "&".join("%s=%s" % (k, v) for k, v in data.items())
        return self.client.put(
            url, data=body, content_type=CONTENT_TYPE, **kwargs)

    def delete(self, url_path, params=None, **kwargs):
        if not params:
            params = {}
        self._update_params(url_path, params, {})
        url = "%s?%s" % (url_path, "&".join("%s=%s" % (k, v) for k, v in params.items()))
        return self.client.delete(url, **kwargs)

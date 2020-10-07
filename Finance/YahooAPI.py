import requests
import json
import urllib

YAHOO_url =""

class YahooAPI(object):

    # def __init__(self, network):
    #     self.network = network

    def __init__(self, url, path=None, params=None,
    timeout = 10, opener=None, force_slash=False, extra_headers=None):

        if not url:
            raise ValueError('Yahoo API needs URL. ')

        if path is None: path = []
        if params is None: param = {}
        if extra_headers is None: extra_headers = {}

        self._extra_headers = extra_headers
        self._url = url
        self._params = params
        self._path = path
        self._timeout = timeout



        # def get

        


# -*- coding: utf-8 -*-
import urllib

class AirbnbRequestBuilder:

    BASE_URL = 'https://api.airbnb.com/v2'


    def __init__(self, client_id, locale='en-US', currency='USD'):
        self.client_id = client_id
        self.locale = locale
        self.currency = currency

    def user(self, user_id):
        endpoint = 'users/%s' % user_id
        return self._build_request('GET', endpoint, {})

    def user_listings(self, user_id, limit=50, offset=0):
        params = {
            'user_id': user_id,
            '_limit': limit,
            '_offset': offset
        }
        return self._build_request('GET', 'listings', params)

    def _build_request(self, method, endpoint, params):
        params['_format'] = 'v1_legacy_show'
        params['client_id'] = self.client_id
        params['locale'] = self.locale
        params['EUR'] = self.currency
        url = '%s/%s?%s' % (self.BASE_URL, endpoint, urllib.urlencode(params))
        return {'method': method, 'url': url}

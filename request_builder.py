# -*- coding: utf-8 -*-
import urllib

class AirbnbRequestBuilder:

    BASE_URL = 'https://api.airbnb.com/v2'

    def __init__(self, client_id, locale='en-US', currency='USD'):
        self.client_id = client_id
        self.locale = locale
        self.currency = currency

    def user(self, user_id, api_format='v1_legacy_show'):
        params = {
            '_format' : api_format
        }
        endpoint = 'users/%s' % user_id
        return self._build_request('GET', endpoint, params)

    def user_listings(self, user_id, limit=50, offset=0, api_format='v1_legacy_long'):
        params = {
            'user_id': user_id,
            '_limit': limit,
            '_offset': offset,
            '_format' : api_format
        }
        return self._build_request('GET', 'listings', params)

    def _build_request(self, method, endpoint, params):
        params['client_id'] = self.client_id
        params['locale'] = self.locale
        params['currency'] = self.currency
        params['_format'] = 'v1_legacy_show'
        url = '%s/%s?%s' % (self.BASE_URL, endpoint, urllib.urlencode(params))
        return {'method': method, 'url': url}

# -*- coding: utf-8 -*-
import urllib

class AirbnbRequestBuilder:

    BASE_URL = 'http://api.airbnb.com/v2'

    def __init__(self, client_id, locale='en-US', currency='USD'):
        self.client_id = client_id
        self.locale = locale
        self.currency = currency

    def user(self, user_id, api_format='v1_legacy_show'):
        params = {
            '_format': api_format
        }
        endpoint = 'users/%s' % user_id
        return self._build_request('GET', endpoint, params)

    def user_reviews(self, user_id, role='all', limit=50, offset=0, api_format='for_mobile_client'):
        params = {
            'reviewee_id': user_id,
            'role': role,
            '_limit': limit,
            '_offset': offset,
            '_format': api_format
        }
        return self._build_request('GET', 'reviews', params)

    def user_owned_listings(self, user_id, limit=50, offset=0, api_format='v1_legacy_long'):
        params = {
            'user_id': user_id,
            '_limit': limit,
            '_offset': offset,
            '_format': api_format
        }
        return self._build_request('GET', 'listings', params)

    def listing(self, listing_id, api_format='v1_legacy_for_p3'):
        params = {
            '_format': api_format
        }
        endpoint = 'listings/%s' % listing_id
        return self._build_request('GET', endpoint, params)

    def _build_request(self, method, endpoint, params):
        params['client_id'] = self.client_id
        params['locale'] = self.locale
        params['currency'] = self.currency
        url = '%s/%s?%s' % (self.BASE_URL, endpoint, urllib.urlencode(params))
        return {'method': method, 'url': url}

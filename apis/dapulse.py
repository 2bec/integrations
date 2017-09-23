# -*- coding: utf-8 -*-

import os
import logging
import datetime
import pytz
import json
import requests


DAPULSE_BASE_URL = "https://api.dapulse.com:443"
DAPULSE_ENDPOINTS = {
	'v1': {
		'users': 'v1/users.json', # Get all users
		'updates': 'v1/updates.json', # Get all users
		'pulses': 'v1/pulses.json', # Get all the account's pulses
	},
}

logger = logging.getLogger()


def utc_now():
	return datetime.datetime.now(tz=pytz.utc)


class DaPulse(object):
	''' DaPulse wrapper '''

	def __init__(self, api_key=None, api_version='v1', endpoints=DAPULSE_ENDPOINTS):

		if api_key is None:
			raise Exception('Needed API KEY.')

		if not type(endpoints) == dict:
			raise Exception('Malformated endpoints url.')

		self.api_key = api_key
		self.api_version = api_version
		self.endpoints = endpoints
		self.headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
		self.data = {'api_key': self.api_key}

	def get(self, endpoint):
		''' get transaction '''
		r = requests.get(endpoint, params=self.data, headers=self.headers)
		if r.status_code == 200:
			data = json.loads(r.content.decode('utf-8'))
			return data
		return []

	def post(self, endpoint):
		''' get transaction '''
		r = requests.get(endpoint, params=self.data, headers=self.headers)
		if r.status_code in [200, 201, 204]:
			data = json.loads(r.content.decode('utf-8'))
			return data
		return []

	def parse_request(self, data):
		pass
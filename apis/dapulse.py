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
		'users': 'v1/users.json',
		'user': 'v1/users/%(user_id)s.json',
		'user_posts': 'v1/users/%(user_id)s/posts.json',
		'user_newsfeed': 'v1/users/%(user_id)s/newsfeed.json',
		'user_unread_feed': 'v1/users/%(user_id)s/unread_feed.json',
		'updates': 'v1/updates.json',
		'update': 'v1/updates/%(update_id)s.json',
		'pulses': 'v1/pulses.json',
		'pulse': 'v1/pulses/%(pulse_id)s.json',
		'pulse_subscribers': 'v1/pulses/%(pulse_id)s/subscribers.json',
		'pulse_notes': 'v1/pulses/%(pulse_id)s/notes.json',
		'pulse_updates': 'v1/pulses/%(pulse_id)s/updates.json',
		'boards': 'v1/boards.json',
		'board': 'v1/boards/%(board_id)s.json',
		'board_groups': 'v1/boards/%(board_id)s/groups.json',
		'board_columns': 'v1/boards/%(board_id)s/columns.json',
		'board_columns_value': 'v1/boards/%(board_id)s/columns/{column_id}/value.json',
		'board_pulses': 'v1/boards/%(board_id)s/pulses.json',
		'board_subscribers': 'v1/boards/%(board_id)s/subscribers.json',
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

	def endpoint_factory(self, **kwargs):
		'''	factory	'''
		endpoint = self.endpoints[self.api_version][kwargs.pop('location_key')]
		# kwargs to format a url
		url_dict = {}
		url_dict.update(kwargs)
		# merge and join to complete url endpoint
		endpoint = endpoint % url_dict
		endpoint = os.path.join(DAPULSE_BASE_URL, endpoint)
		return endpoint

	def get(self, **kwargs):
		''' get transaction '''
		endpoint = self.endpoint_factory(**kwargs)
		r = requests.get(endpoint, params=self.data, headers=self.headers)

		if r.status_code == 200:
			data = json.loads(r.content.decode('utf-8'))
			return data

		return []

	# def post(self, endpoint):
	# 	''' post transaction '''
	# 	r = requests.get(endpoint, data=self.data, headers=self.headers)

	# 	if r.status_code in [200, 201, 204]:
	# 		data = json.loads(r.content.decode('utf-8'))
	# 		return data

	# 	return []

	# def put(self, endpoint):
	# 	''' put transaction '''
	# 	r = requests.put(endpoint, data=self.data, headers=self.headers)
	# 	if r.status_code in [200, 201, 204]:
	# 		data = json.loads(r.content.decode('utf-8'))
	# 		return data
	# 	return []

	# def delete(self, endpoint):
	# 	''' delete transaction '''
	# 	r = requests.delete(endpoint, params=self.data, headers=self.headers)
	# 	if r.status_code in [200, 201, 204]:
	# 		data = json.loads(r.content.decode('utf-8'))
	# 		return data
	# 	return []

	# Users
	def get_users(self):
		url_kwargs = {}
		url_kwargs.update({'location_key': 'users'})
		response = self.get(**url_kwargs)
		return response

	def get_user(self,  user_id):
		url_kwargs = {}
		url_kwargs.update({'user_id': user_id})
		url_kwargs.update({'location_key': 'user'})
		response = self.get(**url_kwargs)
		return response

	# Updates
	def get_updates(self):
		url_kwargs = {}
		url_kwargs.update({'location_key': 'updates'})
		response = self.get(**url_kwargs)
		return response

	def get_update(self, update_id):
		url_kwargs = {}
		url_kwargs.update({'update_id': update_id})
		url_kwargs.update({'location_key': 'update'})
		response = self.get(**url_kwargs)
		return response

	# Pulses
	def get_pulses(self):
		url_kwargs = {}
		url_kwargs.update({'location_key': 'pulses'})
		response = self.get(**url_kwargs)
		return response

	def get_pulse(self, pulse_id):
		url_kwargs = {}
		url_kwargs.update({'pulse_id': pulse_id})
		url_kwargs.update({'location_key': 'pulse'})
		response = self.get(**url_kwargs)
		return response

	def get_pulse_subscribers(self, pulse_id):
		url_kwargs = {}
		url_kwargs.update({'pulse_id': pulse_id})
		url_kwargs.update({'location_key': 'pulse_subscribers'})
		response = self.get(**url_kwargs)
		return response

	def get_pulse_notes(self, pulse_id):
		url_kwargs = {}
		url_kwargs.update({'pulse_id': pulse_id})
		url_kwargs.update({'location_key': 'pulse_notes'})
		response = self.get(**url_kwargs)
		return response

	def get_pulse_updates(self, pulse_id):
		url_kwargs = {}
		url_kwargs.update({'pulse_id': pulse_id})
		url_kwargs.update({'location_key': 'pulse_updates'})
		response = self.get(**url_kwargs)
		return response

	# Boards	
	def get_boards(self):
		url_kwargs = {}
		url_kwargs.update({'location_key': 'boards'})
		response = self.get(**url_kwargs)
		return response

	def get_board(self, board_id):
		url_kwargs = {}
		url_kwargs.update({'board_id': board_id})
		url_kwargs.update({'location_key': 'board'})
		response = self.get(**url_kwargs)
		return response

	def get_board_groups(self, board_id):
		url_kwargs = {}
		url_kwargs.update({'board_id': board_id})
		url_kwargs.update({'location_key': 'board_groups'})
		response = self.get(**url_kwargs)
		return response

	def get_board_columns(self, board_id):
		url_kwargs = {}
		url_kwargs.update({'board_id': board_id})
		url_kwargs.update({'location_key': 'board_columns'})
		response = self.get(**url_kwargs)
		return response

	def get_board_column_value(self, board_id, column_id):
		url_kwargs = {}
		url_kwargs.update({'board_id': board_id})
		url_kwargs.update({'column_id': column_id})
		url_kwargs.update({'location_key': 'board_column_value'})
		response = self.get(**url_kwargs)
		return response

	def get_board_pulses(self, board_id):
		url_kwargs = {}
		url_kwargs.update({'board_id': board_id})
		url_kwargs.update({'location_key': 'board_pulses'})
		response = self.get(**url_kwargs)
		return response

	def get_board_subscribers(self, board_id):
		url_kwargs = {}
		url_kwargs.update({'board_id': board_id})
		url_kwargs.update({'location_key': 'board_subscribers'})
		response = self.get(**url_kwargs)
		return response

	def parse_request(self, data):
		pass
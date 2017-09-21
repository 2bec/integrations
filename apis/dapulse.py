# -*- coding: utf-8 -*-

import datetime
import pytz
import json
import requests


DAPULSE_API_KEY = "22c45794274555a13fc35ce4d0a0a41b"
START_MESSAGE = "Bom dia! Já estou aqui. No aguardo mestre."


def utc_now():
	return datetime.datetime.now(tz=pytz.utc)


class DapulseBot():

	def __init__(self, api_key=DAPULSE_API_KEY):
		self.api_key = api_key

	def start(self, message):
		self.sendMessage(chat_id=message.chat_id, text=START_MESSAGE)

	def get_pulses(self, board_id):
		r = requests.get("https://api.dapulse.com:443/v1/boards/"+ board_id +"/pulses.json?api_key=" + self.api_key) # api_key
		if r.status_code == 200:
			data = json.loads(r.content.decode('utf-8'))
			return data
		return []

	def add_pulse(self, pulse):
		'''
		@pulse = {
			board_id: ,
			user_id: ,
			name: ,
			photo_from_url: ,
			update: {
				text: "Task add from bot",
				announcement: True,
			},
			group_id: ,
		}
		'''
		url = "https://api.dapulse.com:443/v1/boards/%(board_id)s/pulses.json?api_key=%(api_key)s" % {
			'board_id': pulse.get('board_id'),
			'api_key': self.api_key
		} # board_id, api_key
		payload = {
			"pulse": {
				"name": pulse.get('name')
			},
			"user_id": pulse.get('user_id'),
			"group_id": pulse.get('group_id'),
		}

		r = requests.post(url, data=json.dumps(payload))
		if r.status_code == 201:
			return "Added pulse: %s" % pulse
		return "Error! Code: " + str(r.status_code)

	def parse_request(self, data):
		pass
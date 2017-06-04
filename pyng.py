#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import requests

SITE = '<your-site>'
TOKEN = '<your-bot-token>'
URL = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
CHAT_ID = '<your-chat-id>'

def load_prv_state():
    try:
        with open(os.path.join(sys.path[0], 'state.txt'), 'r') as state_file:
            if state_file.read() == 'True':
                state = True
            else:
                state = False
    except IOError:
        print('State file not found. Creating new.')
        # First time running. If site is down inform user.
        state = ping()
        store_new_state(state)
        if not state:
            send_message('Site is down :(')
    return state
    

def store_new_state(state):
    with open(os.path.join(sys.path[0], 'state.txt'), 'w') as state_file:
        state_file.write(str(state))

def ping(site=SITE):
    try:
        requests.get(site).status_code
    except requests.exceptions.ConnectionError:
        state = False
    else:
        state = True
    return state

def send_message(text, chat_id=CHAT_ID):
    msg_params = {'text': text, 'chat_id': chat_id}
    requests.get(URL, params=msg_params)

def main():
    state = ping()
    if state != load_prv_state():
        store_new_state(state)
        if state:
            send_message('Site is up again! :D')
        else:
            send_message('Site is down :(')


if __name__ == '__main__':
    main()
    send_message('run')
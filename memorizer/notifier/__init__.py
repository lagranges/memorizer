#! /usr/bin/env python3
import os
from slack import WebClient
from slack.errors import SlackApiError
from ..tools import now
slack_client = WebClient(token=os.environ["SLACK_API_TOKEN"])
CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]

def send_message(message):
    try:
        slack_client.chat_postMessage(
            channel=CHANNEL_ID,
            text=message
        )
    except SlackApiError as e:
        print(e)
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

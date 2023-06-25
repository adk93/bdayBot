# Standard library imports
import os

# Third party  imports
import slack
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_TOKEN")


def post_message(channel: str, text: str) -> ['str', 'str']:
    try:
        client = slack.WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=text)

        return "OK",
    except Exception as e:
        return "Error", e


def get_users():
    return slack.WebClient(token=SLACK_TOKEN).users_list()


import os
import logging

from slack_sdk.web import WebClient
from slack_sdk.socket_mode import SocketModeClient

################################################################################

AppToken = os.getenv("SLACK_SOCKET_TOKEN")
SlackToken = os.getenv("SLACK_WEB_CLIENT_TOKEN")

# Initialize SocketModeClient with an app-level token + WebClient
client = SocketModeClient(
    # This app-level token will be used only for establishing a connection
    app_token=AppToken,
    # You will be using this WebClient for performing Web API calls in listener
    web_client=WebClient(token=SlackToken),
)

################################################################################

# Logging configuration
logger = logging.getLogger("slackbot")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

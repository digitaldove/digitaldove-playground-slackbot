import logging
from textwrap import dedent

from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.socket_mode.request import SocketModeRequest


logger = logging.getLogger("slackbot")


def slashHandler(client: SocketModeClient, req: SocketModeRequest):

    """
    Handles all slash commands
    Usage: /bot
    """

    # Debugging purpose
    logger.debug(req.payload)

    # I'm just gonna acknowledge all requests
    response = SocketModeResponse(envelope_id=req.envelope_id)
    client.send_socket_mode_response(response)

    postResponse = client.web_client.chat_postMessage(
        text="Greetings!",
        channel=req.payload["channel_id"],
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": dedent(
                        f"Greetings <@{req.payload['user_id']}>, "
                        f"you have invoked `{req.payload['command']}`!"
                    ),
                },
            }
        ],
    )

    # Debugging purpose
    logger.debug(postResponse)

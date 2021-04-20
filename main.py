import logging
from threading import Event

from settings import client
from handler.slash import slashHandler

logger = logging.getLogger("slackbot")

################################################################################

client.socket_mode_request_listeners.append(slashHandler)

# Establish a WebSocket connection to the Socket Mode servers
client.connect()
logger.info("Digitaldove is listening via websocket")

################################################################################

# Event-listening loop
try:
    Event().wait()
except KeyboardInterrupt:
    logger.info("Shutting down...")
except Exception as e:
    logger.error(str(e))

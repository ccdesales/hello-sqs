import os
import logging

from flask import Flask, request
application = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@application.route('/download_the_internet', methods=['GET', 'POST'])
def download_the_internet():
    logger.debug("I've downloaded the Internet")

    return "I've downloaded the Internet"


if __name__ == "__main__":
    application.debug = True
    application.run()

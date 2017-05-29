import os
import logging

from flask import Flask, request
application = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@application.route('/download_the_internet', methods=['POST'])
def download_the_internet():
    content = request.get_data()
    logger.debug('content: %s', content)

    return "I've downloaded the Internet"


if __name__ == "__main__":
    application.debug = True
    application.run()

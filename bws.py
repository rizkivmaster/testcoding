
import subprocess
subprocess.call(['rm','/home/rrangkuti/web/bayarkan/memory'])

from common import logger_factory
from flask.app import Flask
from controllers import home_controller
import os

logger = logger_factory.create_logger(__name__)
logger.info('starting up...')

main = Flask(__name__)
main.secret_key = os.urandom(24)
main.register_blueprint(home_controller.home_router, url_prefix='/')
if __name__ == '__main__':
    main.run(port=29000)

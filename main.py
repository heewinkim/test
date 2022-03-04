from flask import Flask
import logging



application = Flask(__name__)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
fileHandler = logging.FileHandler('/home/ubuntu/test.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(level=logging.DEBUG)


@application.route("/v1/test/hello")
def test_func():
    logger.info('request occurred!')
    return 'hello world'


if __name__ == '__main__':

    application.run('0.0.0.0',port=5000)

from flask import Flask
import logging



app = Flask(__name__)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
fileHandler = logging.FileHandler('test.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(level=logging.DEBUG)


@app.route("/v1/test/hello")
def test_func():
    logger.info('request occurred!')
    return 'hello snaps'


if __name__ == '__main__':

    app.run('0.0.0.0',port=5500)
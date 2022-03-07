from flask import Flask
import os
import logging

application = Flask(__name__)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')

fileHandler = logging.FileHandler(f'{os.path.expanduser("~")}/test.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(level=logging.DEBUG)


@application.route("/v1/test")
@application.route("/v1/test/hello")
def test_func():
    logger.info('request occurred!')
    return 'hello snaps'


@application.route('/index.html')
@application.route('/')
def index():
    return '''<!DOCTYPE HTML><html>
  <head>
    <title>Snaps Test Application</title>
  </head>
  <body>
    <h1>Hello Snaps!</h1>
  </body>
</html>'''

if __name__ == '__main__':

    application.run('0.0.0.0',port=5000)

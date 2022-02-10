from flask import Flask


app = Flask(__name__)

@app.route("/v1/test/hello")
def test_func():
    return 'hello snaps'


if __name__ == '__main__':

    app.run('0.0.0.0',port=5000)
""" app.py """

from flask import Flask, render_template
import requests


app = Flask(__name__)


def get_time():
    response = requests.get('http://localhouse:3001/time')
    return response.json().get('datetime')


def get_user():
    response = requests.get('http://localhost:3002/user')
    return response.json().get('name')


@app.errorhandler(500)
def page_not_found(_):
    return 'Server error', 500


@app.route("/")
def hello():
    time = get_time()
    name = get_user()
    return render_template('hello.html', name=name, time=time)


if __name__ == "__main__":
    app.run(port=3000, debug=True)

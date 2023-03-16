import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


endpoints = ("one", "two", "three", "four", "five", "error")


@app.route('/')
@metrics.do_not_track()
def main():
    return 'Hello world' # metrics are not collected

@app.route("/one")
def first_route():
    time.sleep(random.random() * 0.1)
    return "ok"


@app.route("/two")
def the_second():
    time.sleep(random.random() * 0.2)
    return "ok"


@app.route("/three")
def test_3rd():
    time.sleep(random.random() * 0.3)
    return "ok"


@app.route("/four")
def fourth_one():
    time.sleep(random.random() * 0.4)
    return "ok"


@app.route("/error")
def oops():
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)

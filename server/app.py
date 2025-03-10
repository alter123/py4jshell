import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, logging as flask_logger, request
from formatter import ShellishFormatter

app = Flask(__name__)

@app.before_request
def log_request():
    return None


@app.get("/hello")
def hello():
    app.logger.info("Headers: {}".format(request.headers))
    return "Hello, World!"

if __name__ == "__main__":
    flask_logger.default_handler.setFormatter(ShellishFormatter())
    app.logger.setLevel(logging.INFO)
    app.run('0.0.0.0', port=5000)

from flask import Flask


app = Flask(__name__)

from epl import routes, data
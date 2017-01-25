import os
from flask import Flask, Response, Request
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
client = TwilioRestClient()

if __name__ == '__main__':
	app.run(debug=True)
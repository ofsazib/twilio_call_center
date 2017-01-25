import os
from flask import Flask, Response, Request
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
client = TwilioRestClient()


# This should be the Twilio number.
CUSTOMER_SERVICE_NUMBER = os.environ.get('CUSTOMER_SERVICE_NUMBER','')
# First agent,s phone number
AGENT1_NUMBER = os.environ.get('AGENT1_NUMBER','')
# First agent,s phone number
AGENT2_NUMBER = os.environ.get('AGENT2_NUMBER','')
# Ngrok url
BASE_URL = os.environ.get('BASE_URL', 'http://75ad30f0.ngrok.io')

@app.route('/call', methods=['POST'])
def inbound_call():
    call_sid = request.form['CallSid']
    response = twiml.Response()
    response.dial().conference(call_sid)
    call = client.calls.create(to=AGENT1_NUMBER,
                               from_=CUSTOMER_SERVICE_NUMBER,
                               url=BASE_URL + '/conference/' + call_sid)
    return Response(str(response), 200, mimetype="application/xml")

if __name__ == '__main__':
	app.run(debug=True)
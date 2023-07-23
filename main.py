
from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.before_request
def get_cookie_token_data():
    cookie_token_data = request.cookies.get('token')
    print(cookie_token_data)

# This just tells the client that it is compatible without checking, it would usually check through the cookie data
@app.route('/mco/client/compatible')
def client_compatible():
    return 'COMPATIBLE'

# This is just needed, or realms wont work
@app.route('/mco/available')
def available():
    return 'true'

# Hardcoded list of pending invites
PENDING_INVITES = [
    {
        "invitationId": "1",
        "worldName": "I am trolling the realms system",
        "worldDescription": "no.",
        "worldOwnerName": "Notch",
        "worldOwnerUuid": "069a79f444e94726a5befca90e38aaf5",
        "date": 1 # Unix timestamp
    }
]

# Even tho its s literally just the Realms, or Servers
@app.route('/worlds')
def worlds():
    # Load server data from JSON file
    with open('server.json') as file:
        data = json.load(file)

    # Return the server data as a JSON response
    return json.dumps(data)

# Sends a list of invites
@app.route('/invites/pending')
def get_pending_invites():
    return jsonify({'invites': PENDING_INVITES})

# Depending on the id, it will send a regular server address
@app.route('/worlds/v1/<int:id>/join/pc', methods=['GET'])
def get_server_address(id):
    # This implements basic logic of id's (look at the server json)
    if id == 1:
        server_address = '127.0.0.1:25565' # example address, replace with actual address
        return jsonify({
           'address': server_address,
           'pendingUpdate': False
        })
    else:
        return jsonify({
           'address': "hypixel.net",
           'pendingUpdate': False
        })

# Figured this out, maybe we should have an admin panel to change this
@app.route('/mco/v1/news')
def realms_news():
    return jsonify({'newsLink': 'https://bunker.mt'})

# I dont know if this works
@app.route('/activities/liveplayerlist')
def liveplayerlist():
    return '1'

# 'true' tells the client that they have a free 30 day trial of realms (lol no)
@app.route('/trial')
def trial():
    return 'true'

# This doesnt work, im suspecting the client needs to recieve a confirmation
@app.route('/trial', methods=['POST'])
def trialpostedition():
    # get the JSON data from the POST request
    data = request.get_json()

    # print the data to the console
    print(data)

    response = jsonify({'status': 'success'})
    return response

@app.route('/invites/count/pending')
def invitecount():
    return '2'

if __name__ == '__main__':
    app.run(port=8000)
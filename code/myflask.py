import json
from flask import Flask, request, jsonify
app = Flask(__name__)

# python -m flask --app myflask run

@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@wunderland.com'})

## curl -X POST http://127.0.0.1:5000/user -H 'Content-Type: application/json' -d '{"login":"my_login","password":"my_password"}'
@app.route('/user', methods=['POST'])
def user():
    with open('file.json', 'a') as f:
        json.dump(request.json, f)
    return jsonify(request.json)

app.run()

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name')  # URI에 있는 path parameter를 가져온다 ?user_name=<name>
    if username == 'aiden':  # /login?user_name=aiden
        return_data = {'auth':True}
    else:
        return_data = {'auth':False}
    return jsonify(return_data)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8089')
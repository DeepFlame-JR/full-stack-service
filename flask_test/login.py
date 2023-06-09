from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name')  # URI에 있는 path parameter를 가져온다 ?user_name=<name>
    if username == 'aiden':  # /login?user_name=aiden
        return_data = {'auth':True}
    else:
        return_data = {'auth':False}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8089')
from flask import Flask, jsonify, request, render_template
app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def login():
    address = request.args.get('address')
    passwd = request.args.get('passwd')
    print(address, passwd)
    
    if address == 'aiden@gmail.com':  # /login?user_name=aiden
        return_data = {'auth':True}
    else:
        return_data = {'auth':False}
    return jsonify(return_data)


@app.route('/login_html')
def hello_html():
    return render_template('login_index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8089')
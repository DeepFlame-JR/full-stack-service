from flask import Flask, jsonify, request, render_template, make_response
# 하나의 웹사이트는 다른 서버에 있는 정보를 가져올 수 있음
# 하지만 script 내에서는 HTTP request는 다른 서버에서 가져올 수 없음 (Same Origin Policy)
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # request/response Header에 CORS 지원 헤더 정보를 넣어줌 (Access-Control-Allow-Origin: *)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        data = request.get_json()
        print(f"[POST] {data['email']}")
    elif request.method == 'GET':
        user = request.args.get('email')
        print(f"[GET] {user}")
    return make_response(jsonify({'success':True}), 200)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8089')
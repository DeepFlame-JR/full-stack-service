from flask import Flask, jsonify, request, render_template, make_response
import requests

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 error</h1>", 404

@app.before_first_request
def before_first_request():
    print('flask 실행 후 첫 요청 때 실행')
    
@app.before_request
def before_request():
    print("HTTP 요청이 들어올 때마다 실행")
    
@app.after_request
def after_request(response):
    print("HTTP 요청 처리가 끝나고 브라우저에 응당하기 전에 실행")
    return response

@app.route('/test')
def get_test():
    return "test"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8089', debug=True)
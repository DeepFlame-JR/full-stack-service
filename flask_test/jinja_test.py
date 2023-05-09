from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_jinja(user):
    values = ['content1', 'content2', 'content3']
    return render_template('jinja.html', name=user, values=values, data=27)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8089')
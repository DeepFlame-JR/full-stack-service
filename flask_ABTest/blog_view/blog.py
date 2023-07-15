from flask import Flask, Blueprint, request, render_template

blog_abtest = Blueprint('blog', __name__, url_prefix='/blog')

@blog_abtest.route('/test')
def test():
    return render_template('blogA.html')
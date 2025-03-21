from flask import Flask, render_template ,url_for
from markupsafe import escape
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name/<username>')
def user(username):
    return f"Hello {escape (username)}"

@app.route('/id')
def id():
    return f"Hello ID"
    
if __name__ == "__main__":
    app.run(debug=True)
with app.test_request_context():
    print(url_for('index'))
    print(url_for('user', username='GDs'))
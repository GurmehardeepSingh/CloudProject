from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    log_request()  # Log request details
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    log_request()
    return "About Us"

@app.route('/user/<username>')
def user(username):
    log_request()
    return f"Welcome {username}"

def log_request():
    """Logs the request details."""
    client_ip = request.remote_addr  # Get IP address
    user_agent = request.headers.get('User-Agent')  # Get User-Agent info
    requested_url = request.path  # Get requested URL

    log_message = f"Access from {client_ip} | URL: {requested_url} | Agent: {user_agent}"
    print(log_message)  # Print to terminal (optional: save to file)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

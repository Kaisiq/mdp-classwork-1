import socket
from flask import Flask
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)  # Compliant


@app.route('/')
def hello_world():
    return "Flask running on {}".format(socket.gethostname())


if __name__ == '__main__':
    # Note the extra host argument. If we didn't have it, our Flask app
    # would only respond to requests from inside our container
    app.run(host='0.0.0.0')

import unittest
import socket
from flask import Flask
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)  # Compliant


@app.route('/')
def hello_world():
    return "Flask running on {}".format(socket.gethostname())


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

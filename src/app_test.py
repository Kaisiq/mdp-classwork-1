import unittest

from . import app


class TestApp(unittest.TestCase):
    def test_number_one(self):
        with app.test_client() as client:
        rv = client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

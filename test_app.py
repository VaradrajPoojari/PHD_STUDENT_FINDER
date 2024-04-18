import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_post_request_response(self):
        # Send a POST request with text data
        response = self.app.post('/response', data={'text': 'Physics'})
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected message
    #     self.assertIn(b'Your message was received: Hello, World!', response.data)

    # def test_input_is_string(self):
    #     # Input to the function is a string
    #     input_text = 'Hello, World!'
    #     # Check if the input is a string
    #     self.assertIsInstance(input_text, str)

if __name__ == '__main__':
    unittest.main()

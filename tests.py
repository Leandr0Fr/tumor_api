import unittest
from app import app
from unittest.mock import MagicMock

class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping_endpoint(self):
        # Realiza un ping al servidor
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
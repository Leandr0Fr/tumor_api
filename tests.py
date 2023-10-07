import unittest
from app import app, predict
from unittest.mock import MagicMock
from flask import Request
class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping_endpoint(self):
        # Realiza un ping al servidor
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)
    
    def test_predict_valid_image_returns_200(self):
        # Simula una solicitud POST con una imagen válida
        with open('image_test/no_tumor.jpg', 'rb') as image_file:
            response = self.app.post('/predict', data={'image': (image_file, 'test.jpg')})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
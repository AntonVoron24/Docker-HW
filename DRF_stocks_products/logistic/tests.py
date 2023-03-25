from unittest import TestCase
from rest_framework.test import APIClient


class TestSampleVeiw(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('/api/v1/sample-view/')
        self.assertEqual(response.data, 'This is checking!')

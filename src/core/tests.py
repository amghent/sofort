from django.test import Client, TestCase
from django.urls import reverse


class TestIndex(TestCase):
    def setup(self):
        self.client = Client()

    def test_index(self):
        self.setup()

        response = self.client.get("/")

        assert response.status_code == 200

    def test_index_reverse(self):
        response = self.client.get(reverse("index"))

        assert response.status_code == 200

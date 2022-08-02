from django.test import Client, TestCase
from django.urls import reverse


class TestIndex(TestCase):
    def test_index(self):
        client = Client()
        response = client.get("/")

        assert response.status_code == 200

    def test_index_reverse(self):
        client = Client()
        response = client.get(reverse("index"))

        assert response.status_code == 200

from django.test import TestCase


class TestOcLettingsSite(TestCase):
    def test_access_homepage(client):
        """
        test access to homepage
        """
        response = client.get("/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Welcome to Holiday Homes" in response.content.decode("utf-8")

    def test_access_unavailable_page(client):
        """
        test access on an unavailable page
        """
        response = client.get('/unavailable_page')
        output = response.status_code
        expected = 404
        assert output == expected
        assert "La page demandée n'existe pas" in response.content.decode("utf-8")

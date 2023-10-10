from django.test import TestCase, Client


class TestOcLettingsSite(TestCase):

    def setUp(self):
        self.client = Client()

    def test_access_homepage(self):
        """
        test access to homepage
        """
        response = self.client.get("/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Welcome to Holiday Homes" in response.content.decode("utf-8")

    def test_access_unavailable_page(self):
        """
        test access on an unavailable page
        """
        response = self.client.get('/unavailable_page')
        output = response.status_code
        expected = 404
        assert output == expected
        assert "La page demandée n'existe pas" in response.content.decode("utf-8")

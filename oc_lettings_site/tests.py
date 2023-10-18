from django.test import TestCase, Client


class TestOcLettingsSite(TestCase):

    def setUp(self):
        self.client = Client()

    def test_access_homepage(self):
        """
        test access to homepage
        INPUT : valid url '/'
        EXPECTED OUTPUT : status code 200 + words 'Welcome to Holiday Homes' response page
        """
        response = self.client.get("/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Welcome" in response.content.decode("utf-8")

    def test_access_unavailable_page(self):
        """
        test access on an unavailable page
        INPUT : invalid url '/unavailable_page'
        EXPECTED OUTPUT : status code 404 + words 'La page demandée n'existe pas' response page
        """
        response = self.client.get('/unavailable_page')
        output = response.status_code
        expected = 404
        assert output == expected
        assert "La page demandée n'existe pas" in response.content.decode("utf-8")

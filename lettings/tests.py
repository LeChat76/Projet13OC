from django.test import TestCase, Client
from .models import Letting, Address


class TestLettings(TestCase):
    """
    class for lettings tests
    """

    def setUp(self):
        """
        init objects for the tests
        """
        self.client = Client()
        Address.objects.create(
            id=666,
            number=666,
            zip_code=666,
        )
        Letting.objects.create(
            id=666,
            title="Joshua Tree Green Haus",
            address_id=666
        )

    def test_access_homepage(self):
        """
        test access to homepage of Lettings
        INPUT : valid url '/lettings/'
        EXPECTED OUTPUT : status code 200 + word 'Lettings' response page
        """
        response = self.client.get("/lettings/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Lettings" in response.content.decode("utf-8")

    def test_access_existing_letting(self):
        """
        test access to an existing letting
        INPUT : valid url '/lettings/666'
        EXPECTED OUTPUT : status code 200 + words 'Joshua Tree Green Haus' in response page
        """
        response = self.client.get("/lettings/666", follow=True)
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Joshua Tree Green Haus" in response.content.decode("utf-8")

    def test_access_unexisting_letting(self):
        """
        test access to an unexisting letting
        INPUT : invalid url '/lettings/6666666'
        EXPECTED OUTPUT : status code 301
        """
        response = self.client.get("/lettings/6666666")
        output = response.status_code
        expected = 301
        assert output == expected
        # assert "La requete n'a pas pu aboutir" in response.content.decode("utf-8")

    def test_access_unavailable_letting_page(self):
        """
        test access to an unexisting letting page
        INPUT : invalid url '/lettings2'
        EXPECTED OUTPUT : status code 404
        """
        response = self.client.get("/lettings2")
        output = response.status_code
        expected = 404
        assert output == expected
        assert "La page demandée n'existe pas" in response.content.decode("utf-8")

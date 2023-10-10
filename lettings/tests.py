import pytest
from django.test import TestCase, Client
from .models import Letting, Address


@pytest.mark.django_db
class TestLettings(TestCase):

    def setUp(self):
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
        """
        response = self.client.get("/lettings/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Lettings" in response.content.decode("utf-8")

    def test_access_existing_letting(self):
        """
        test access to an existing letting
        """
        response = self.client.get("/lettings/666", follow=True)
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Joshua Tree Green Haus" in response.content.decode("utf-8")

    def test_access_unexisting_letting(self):
        """
        test access to an unexisting letting
        """
        response = self.client.get("/lettings/6666666")
        output = response.status_code
        expected = 301
        assert output == expected
        # assert "La requete n'a pas pu aboutir" in response.content.decode("utf-8")

    def test_access_unavailable_letting_page(self):
        """
        test access to an unexisting letting page
        """
        response = self.client.get("/lettings2")
        output = response.status_code
        expected = 404
        assert output == expected
        assert "La page demandée n'existe pas" in response.content.decode("utf-8")

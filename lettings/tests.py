from django.test import TestCase


class TestLettings(TestCase):
    def test_access_homepage(client):
        """
        test access to homepage of Lettings
        """
        response = client.get("/lettings/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Lettings" not in response.content.decode("utf-8")
    
    def test_access_existing_letting(client):
        """
        test access to an existing letting
        """
        response = client.get("/lettings/1")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Joshua Tree Green Haus" not in response.content.decode("utf-8")

    def test_access_unexisting_letting(client):
        """
        test access to an unexisting letting
        """
        response = client.get("/lettings/666666666")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "La requete n'a pas pu aboutir" not in response.content.decode("utf-8")

    def test_access_unavailable_letting_page(client):
        """
        test access to an unexisting letting page
        """
        response = client.get("/lettings2")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "La page demandée n'existe pas" not in response.content.decode("utf-8")
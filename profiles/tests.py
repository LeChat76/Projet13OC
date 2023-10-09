from django.test import TestCase


class TestProfiles(TestCase):
    def test_access_homepage(client):
        """
        test access to homepage of profiles
        """
        response = client.get("/profiles/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Profiles" not in response.content.decode("utf-8")

    def test_access_existing_profile(client):
        """
        test access to an existing profiles
        """
        response = client.get("/profiles/HeadlinesGazer")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "HeadlinesGazer" not in response.content.decode("utf-8")

    def test_access_unexisting_profile(client):
        """
        test access to an unexisting profiles
        """
        response = client.get("/profiles/Cedric_Delauney")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "La requete n'a pas pu aboutir" not in response.content.decode("utf-8")

    def test_access_unexisting_profile_page(client):
        """
        test access to an unexisting profiles page
        """
        response = client.get("/profiles2")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "La page demandée n'existe pas" not in response.content.decode("utf-8")

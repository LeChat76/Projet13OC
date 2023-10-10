import pytest
from django.test import TestCase, Client
from .models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestLettings(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(
            id=666,
            username="MrRobot",
        )
        Profile.objects.create(
            id=666,
            favorite_city="Rouen",
            user_id=666,
        )

    def test_access_homepage(self):
        """
        test access to homepage of profiles
        """
        response = self.client.get("/profiles/")
        output = response.status_code
        expected = 200
        assert output == expected
        assert "Profiles" in response.content.decode("utf-8")

    def test_access_existing_profile(self):
        """
        test access to an existing profiles
        """
        response = self.client.get("/profiles/MrRobot", follow=True)
        output = response.status_code
        expected = 200
        assert output == expected
        assert "MrRobot" in response.content.decode("utf-8")

    def test_access_unexisting_profile(self):
        """
        test access to an unexisting profiles
        """
        response = self.client.get("/profiles/Cedric_Delauney")
        output = response.status_code
        expected = 301
        assert output == expected
        # assert "La requete n'a pas pu aboutir" in response.content.decode("utf-8")

    def test_access_unexisting_profile_page(self):
        """
        test access to an unexisting profiles page
        """
        response = self.client.get("/profiles2")
        output = response.status_code
        expected = 404
        assert output == expected
        assert "La page demandée n'existe pas" in response.content.decode("utf-8")

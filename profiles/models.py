from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This class describe profile of users
    """
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        This application format print output of the profile object
        """
        return self.user.username

    class Meta:
        """
        Meta class to associate class and table in sqlite3 database
        """
        db_table = 'oc_lettings_site_profile'

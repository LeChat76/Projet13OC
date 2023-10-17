from django.db import models
from .address import Address


class Letting(models.Model):
    """
    This class contain address for Lettings application
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        This application format print output of the letting object
        """
        return self.title

    class Meta:
        """
        Meta class to associate class and table in sqlite3 database
        """
        db_table = 'oc_lettings_site_letting'

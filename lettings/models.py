from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    This class describe addresses for the application Lettings
    """
    id = models.AutoField(primary_key=True)
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        This application format print output of the Address object
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta class to associate class and table in sqlite3 database
        Also modify the plural for word 'address'
        """
        db_table = 'oc_lettings_site_address'
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


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

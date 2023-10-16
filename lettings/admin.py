from django.contrib import admin

from .models.letting_model import Letting
from .models.address_model import Address

"""
tables to include in django administration page
"""
admin.site.register(Letting)
admin.site.register(Address)

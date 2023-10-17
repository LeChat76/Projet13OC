from django.contrib import admin

from .models import Letting, Address

"""
tables to include in django administration page
"""
admin.site.register(Letting)
admin.site.register(Address)

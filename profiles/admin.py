from django.contrib import admin

from .models.profile_model import Profile

"""
tables to include in django administration page
"""
admin.site.register(Profile)

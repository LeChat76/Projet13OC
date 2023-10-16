import os
from django.shortcuts import render
from .models.profile_model import Profile
from utils.utils import send_to_sentry


def index(request):
    """
    This definition is used to generate profile index page
    """
    try:
        profiles_list = Profile.objects.all()
    except Profile.DoesNotExist:
        send_to_sentry("profiles", "get_all", "no records found in Profile table")
    context = {'profiles_list': profiles_list}
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    return render(request, template_path, context)


def profile(request, username):
    """
    This definition is used to generate detailed page for a specific profile
    INPUT : username
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        send_to_sentry("profile", "get", f"username {username} does not exists.")
    context = {'profile': profile}
    return render(request, 'profile.html', context)

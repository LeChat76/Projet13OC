import os
from django.shortcuts import render
from .models import Profile


def index(request):
    """
    This definition is used to generate profile index page
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    return render(request, template_path, context)


def profile(request, username):
    """
    This definition is used to generate detailed page for a specific profile
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)

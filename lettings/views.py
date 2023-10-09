import os
from django.shortcuts import render
from .models import Letting


def index(request):
    """
    This fonction is used to generate letting index page
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    return render(request, template_path, context)


def letting(request, letting_id):
    """
    This fonction is used to generate detailed page for a specific address
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)

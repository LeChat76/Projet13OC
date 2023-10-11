import os
from django.shortcuts import render
from .models import Letting
from utils.utils import send_to_sentry


def index(request):
    """
    This fonction is used to generate letting index page
    """
    try:
        lettings_list = Letting.objects.all()
    except Letting.DoesNotExist:
        send_to_sentry("letting", "get_all", "no records found in Letting table")
    context = {'lettings_list': lettings_list}
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    return render(request, template_path, context)


def letting(request, letting_id):
    """
    This fonction is used to generate detailed page for a specific address
    INPUT : letting ID
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        send_to_sentry("letting", "get", f"letting_id {letting_id} does not exists.")
    context = {
        'title': letting.title,
        'address': letting.address,
    }

    return render(request, 'letting.html', context)

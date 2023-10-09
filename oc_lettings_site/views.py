from django.shortcuts import render


def index(request):
    """
    This fonction is used to generate home index page
    """
    return render(request, 'index.html')

from django.shortcuts import render


def index(request):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    """
    return render(request, 'index.html')

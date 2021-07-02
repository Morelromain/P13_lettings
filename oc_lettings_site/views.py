from django.shortcuts import render


def index(request):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    """
    return render(request, 'index.html')


def trigger_error(request):
    """
    Create a division error
    """
    division_by_zero = 1 / 0
    print(division_by_zero)

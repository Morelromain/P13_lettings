from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
def index(request):
    return render(request, 'index.html')


from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    Aenean leo magna, vestibulum et tincidunt fermentum.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'letting/index.html', context)


def letting(request, letting_id):
    """
    Cras ultricies dignissim purus, vitae hendrerit ex varius non.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting/letting.html', context)

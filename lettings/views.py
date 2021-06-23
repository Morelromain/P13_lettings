from django.shortcuts import render

from lettings.models import Letting

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#def index(request):
#    return render(request, 'index.html')


# Aenean leo magna, vestibulum et tincidunt fermentum.
def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'letting/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting/letting.html', context)

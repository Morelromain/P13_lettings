from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    Sed placerat quam in pulvinar commodo.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profile/index.html', context)


def profile(request, username):
    """
    Laoreet neque quis, pellentesque dui.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile/profile.html', context)

from django.shortcuts import render

from profiles.models import Profile

# Sed placerat quam in pulvinar commodo.
def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


# laoreet neque quis, pellentesque dui.
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)

from django.contrib import admin
from django.urls import path, include

from lettings import views as views_l
from profiles import views as views_p
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #path('lettings/', views_l.index, name='lettings_index'),
    #path('lettings/<int:letting_id>/', views_l.letting, name='letting'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),

    path('admin/', admin.site.urls),
]


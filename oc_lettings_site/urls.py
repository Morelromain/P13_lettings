from django.contrib import admin
from django.urls import path

from lettings import views as views_l
from profiles import views as views_p

urlpatterns = [
    path('', views_l.index, name='index'),
    path('lettings/', views_l.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views_l.letting, name='letting'),
    path('profiles/', views_p.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views_p.profile, name='profile'),
    path('admin/', admin.site.urls),
]

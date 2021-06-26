from django.urls import path

from . import views as views_p


app_name = 'profiles'
urlpatterns = [
    path('profiles/', views_p.index, name='index'),
    path('profiles/<str:username>/', views_p.profile, name='profile'),
]

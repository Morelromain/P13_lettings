from django.contrib import admin
from django.urls import path

from . import views as views_p

app_name = 'profiles'

urlpatterns = [
    path('profiles/', views_p.index, name='index'),
    path('profiles/<str:username>/', views_p.profile, name='profile'),
]





"""urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
]"""
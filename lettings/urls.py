from django.contrib import admin
from django.urls import path

from . import views as views_l

app_name = 'lettings'

urlpatterns = [
    path('lettings/', views_l.index, name='index'),
    path('lettings/<int:letting_id>/', views_l.letting, name='letting'),
]


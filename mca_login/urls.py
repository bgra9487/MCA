from django.urls import path
from mca_login import views

urlpatterns = [
    path('', views.simple, name='index')
]
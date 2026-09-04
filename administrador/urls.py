from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_admin, name='index_admin'),
]
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    # Create a path object defining the URL pattern to the index view
    path(route='', view=views.index, name='index'),
    path(route='date', view=views.get_date,name='date'),
]
from django.urls import path

from . import views

urlpatterns = [
    # linking the views to a url path
    path('', views.index, name='index'),
]
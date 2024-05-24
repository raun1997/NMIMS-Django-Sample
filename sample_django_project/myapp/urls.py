from django.urls import path

from . import views   
# from the same directory,
# import the views

urlpatterns = [
    path("", views.index, name="index"),
]
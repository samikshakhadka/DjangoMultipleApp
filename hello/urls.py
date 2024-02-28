from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("samiksha", views.samiksha, name="samiksha" )
]
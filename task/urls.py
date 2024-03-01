from django.urls import path
from . import views

#creating app_name to prevent namespace collision while redirecting link from <a> tag
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add , name="add")
]
from django.urls import path
from .views import *

urlpatterns = [
    path("", trainee_list, name="trainee_list"),
    path("update/<int:id>", trainee_update, name="trainee_update"),
    path("delete/<int:id>", trainee_delete, name="trainee_delete"),
    path("details/<int:id>", trainee_details, name="trainee_details"),
    path("create/", trainee_create, name="trainee_create"),
]
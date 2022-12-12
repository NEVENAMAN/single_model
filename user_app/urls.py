from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create_Users',views.create_Users),
    path('display_Users',views.display_Users)
]
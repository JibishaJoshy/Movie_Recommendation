from django.urls import path
from FixiApp import views

urlpatterns=[
    path('', views.home_page, name="home"),
]
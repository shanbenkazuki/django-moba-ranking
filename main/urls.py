from django.urls import path

from . import views

urlpatterns = [
    path("", views.hero_ranking, name="hero_ranking"),
]
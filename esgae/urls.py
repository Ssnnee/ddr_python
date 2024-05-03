"""
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('actualite', views.actualite, name="actualite"),
    path('projet', views.projet, name="projet"),
    path('parcours', views.parcours, name="parcours"),
    path('contact', views.contact, name="contact"),
    path('galerie', views.galerie, name="galerie"),
]

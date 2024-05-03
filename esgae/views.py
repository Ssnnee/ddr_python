from django.shortcuts import render


def accueil(request):
    return render(request, "accueil.html")


def actualite(request):
    return render(request, "actualite.html")


def projet(request):
    return render(request, "projet.html")


def parcours(request):
    return render(request, "parcours.html")


def contact(request):
    return render(request, "contact.html")


def galerie(request):
    return render(request, "galerie.html")

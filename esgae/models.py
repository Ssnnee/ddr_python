from django.db import models

# Create your models here.


class Eleve(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    name = models.CharField(max_length=100, unique=True, verbose_name="name")
    prenom = models.CharField(max_length=100, verbose_name="prenom")
    adresse = models.CharField(max_length=100, verbose_name="adresse")
    telephone = models.CharField(max_length=100, verbose_name="telephone")
    genre = models.CharField(max_length=100, verbose_name="genre")

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"


class Livre(models.Model):
    titre = models.CharField(max_length=100, unique=True, verbose_name="titre")
    quantite = models.IntegerField(default=1, verbose_name="quantite")
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, verbose_name="Eleve")
    auteur = models.CharField(max_length=100, verbose_name="auteur")
    prix = models.FloatField(verbose_name="prix")
    id_eleve = models.CharField(max_length=100, verbose_name="id_eleve")
    annee = models.CharField(max_length=100, verbose_name="annee")

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

from django.db import models
from django.utils import timezone
from datetime import timedelta

class Ordinateur(models.Model):
    id = models.AutoField(primary_key=True)
    marque = models.CharField(max_length=255)
    dte_acquisition = models.DateField()
    ram = models.CharField(max_length=255)
    disque_dur = models.CharField(max_length=255)
    processeur = models.CharField(max_length=255)
    ecran = models.IntegerField()
    numero_serie=models.CharField(max_length=255)
    def __str__(self):
        return self.numero_serie

class Personne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    telephone= models.CharField(max_length=255)
    def __str__(self):
        nom_complet=self.nom+" "+self.prenom
        return nom_complet
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

class Panne(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    statut = models.CharField(max_length=255,null=True)
    intitule = models.TextField()
    utilisateur =models.TextField()
    telephone =models.IntegerField()
    numero_seri=models.IntegerField(null=True)
    marque=models.TextField()
    nombre= models.IntegerField()
    departement=models.TextField()
    

class Mouvement(models.Model):
    id = models.AutoField(primary_key=True)
    ordinateur = models.ForeignKey(Ordinateur, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    date = models.DateField()
    #type = models.CharField(max_length=255)
    motifs = models.CharField(max_length=250)

class Licences(models.Model):
    cle = models.CharField(max_length=100, unique=True)
    uses_nbr = models.PositiveIntegerField(default=1)
    expiration_date = models.DateField()
    is_visible = models.BooleanField(default=True)
    
    def is_expiring_soon(self):
        return self.expiration_date - timezone.now().date() <= timedelta(days=7)
    
    def __str__(self):
        return self.cle

class Histo(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True,null=True)
    intitule = models.TextField()
    utilisateur =models.TextField()
    telephone =models.IntegerField()
    marque=models.TextField()
    departement=models.TextField()
    def __str__(self):
        return self.intitule
# models.py
from django.db import models

class Client(models.Model):
    name = models.CharField('Cliente', max_length=50)
    dir1 = models.CharField('Dir 1', max_length=150)
    dir2 = models.CharField('Dir 2', max_length=150)
    dir3 = models.CharField('Dir 3', max_length=150)
    rfc = models.CharField('RFC', max_length=50)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Nom(models.Model):
    name = models.CharField('NOM', max_length=100)
    def __str__(self):
        return self.name

class Part(models.Model):
    number = models.CharField('No de Parte', max_length=100)
    description = models.CharField('Descripción', max_length=200)
    # nom = models.CharField('NOM', max_length=50)
    nom = models.ForeignKey(Nom, on_delete=models.CASCADE, default=1) 
    country = models.CharField('País', max_length=100, default='Mexico')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1) 
    def __str__(self):
        return self.number#, self.description


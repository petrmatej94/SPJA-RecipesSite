from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator


class Fotogalerie(models.Model):
    nazev = models.CharField(max_length=100)
    #fotka = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.nazev


class SvetovaKuchyne(models.Model):
    jmeno = models.CharField(max_length=100)
    popis = models.TextField(max_length=1000, default="popis")

    def __str__(self):
        return self.jmeno


class Chod(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev


class Recept(models.Model):
    jmeno = models.CharField(max_length=200)
    postup = models.TextField(max_length=2000, default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    publikovano = models.DateTimeField(default=datetime.now(), blank=True)
    hodnoceni = models.DecimalField(default=2.5, decimal_places=1, max_digits=3, validators=[MaxValueValidator(5), MinValueValidator(0)])
    svetova_kuchyne = models.ForeignKey(SvetovaKuchyne, on_delete=models.CASCADE, default=0)
    ingredience = models.TextField(max_length=1000, default="")
    chod = models.ForeignKey(Chod, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.jmeno

    def was_published_recenlty(self):
        return self.publikovano >= timezone.now() - datetime.timedelta(days=1)

    def hodnotit(self, bod):
        self.hodnoceni = (self.hodnoceni + bod) / 2

    def celkoveHodnoceni(self):
        all_recepty = Recept.objects.filter(autor=self)
        celkoveHodnoceni = 0
        for recept in all_recepty:
            celkoveHodnoceni = (celkoveHodnoceni + recept.hodnoceni) / 2
        return celkoveHodnoceni


class Komentar(models.Model):
    nadpis = models.CharField(max_length=100)
    text = models.TextField(max_length=300, default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    komentovany_recept = models.ForeignKey(Recept, on_delete=models.CASCADE, default=0)
    publikovano = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.text

    def publikovan_nedavno(self):
        return self.publikovano >= timezone.now() - datetime.timedelta(days=1)


class Zprava(models.Model):
    nadpis = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    odesilatel = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nadpis


class Clanek(models.Model):
    nadpis = models.CharField(max_length=100)
    text = models.TextField(max_length=5000, default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    publikovano = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.nadpis

    def publikovan_nedavno(self):
        return self.publikovano >= timezone.now() - datetime.timedelta(days=1)


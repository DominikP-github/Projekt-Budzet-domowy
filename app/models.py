from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zysk = models.BooleanField()
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nazwa

    @property
    def plan(self):
        return sum(tranzakcja.plan for tranzakcja in self.tranzakcje.all())

    @property
    def realizacja(self):
        return sum(tranzakcja.realizacja for tranzakcja in self.tranzakcje.all())

    @property
    def saldo(self):
        return sum(tranzakcja.saldo for tranzakcja in self.tranzakcje.all())
    
    @property
    def miesiac(self):
        return self.data.month  # Pobieramy miesiąc z daty


class tranzakcje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kategoria = models.ForeignKey(Kategoria, related_name='tranzakcje', on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=180)
    plan = models.FloatField()
    realizacja = models.FloatField()
    saldo = models.FloatField()
    data = models.DateField(default=timezone.now)
    jednorazowa = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nazwa} - {self.kategoria.nazwa} - {self.user.username}"

   

    @property
    def miesiac(self):
        return self.data.month  # Pobieramy miesiąc z daty

    def save(self, *args, **kwargs):
        if self.data <= timezone.now().date():
             if self.data== False:  # Sprawdź, czy data transakcji jest dzisiejsza
                self.realizacja = self.plan  # Zaktualizuj realizację na plan
        super().save(*args, **kwargs)  # Zapisz obiekt do bazy danych
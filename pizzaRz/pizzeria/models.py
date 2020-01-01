# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Lokal(models.Model):
    nazwa_lokalu = models.CharField(max_length=50, blank=True, null=True)
    id_lokalu = models.OneToOneField('Zamowienia', models.DO_NOTHING, db_column='id_lokalu', primary_key=True, related_name='lokalSet')
    miasto = models.CharField(max_length=20, blank=True, null=True)
    cenadostawy = models.CharField(max_length=50, blank=True, null=True)
    adres = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lokal'


class LokalPizzzaLaczaca(models.Model):
    id_lokalu = models.ForeignKey(Lokal, models.DO_NOTHING, db_column='id_lokalu')
    id_pizzy = models.ForeignKey('Pizzza', models.DO_NOTHING, db_column='id_pizzy')

    class Meta:
        managed = True
        db_table = 'lokal_pizzza_laczaca'


class Pizzza(models.Model):
    id_pizzy = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=255, blank=True, null=True)
    skladniki = models.CharField(max_length=255, blank=True, null=True)
    rozmiar = models.IntegerField(blank=True, null=True)
    cena = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pizzza'


class Uzytkownicy(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=70, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    zamowienia = models.OneToOneField('Zamowienia', models.DO_NOTHING, db_column='zamowienia', blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    rola = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'uzytkownicy'


class Zamowienia(models.Model):
    zamowienia = models.IntegerField(blank=True, null=True)
    id_zamowienia = models.AutoField(primary_key=True)
    pizza = models.CharField(max_length=255, blank=True, null=True)
    lokal = models.IntegerField(blank=True, null=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    telefon = models.CharField(max_length=9)
    mail = models.CharField(max_length=30)
    adres = models.CharField(max_length=40)
    uwagi = models.CharField(max_length=250)
    platnosc = models.IntegerField()
    numerkarty = models.CharField(db_column='numerKarty', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cvv = models.CharField(db_column='CVV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mmrr = models.CharField(db_column='MMRR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cena = models.FloatField()

    class Meta:
        managed = True
        db_table = 'zamowienia'

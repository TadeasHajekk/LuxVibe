# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    # Propojení na přihlášeného uživatele z Djanga
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Propojení na produkt
    product = models.ForeignKey('Products', on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'orders'


class Products(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    stock = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    id_druh = models.ForeignKey('Type', models.DO_NOTHING, db_column='id_druh', blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    class Meta:
        managed = True
        db_table = 'products'


class Type(models.Model):
    id_druh = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
from django.contrib import admin
from .models import Users, Products, Type, Orders

# Tímto říkáme administraci, ať nám tyto tabulky zobrazí
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Type)
admin.site.register(Orders)
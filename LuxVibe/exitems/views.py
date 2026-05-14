from django.shortcuts import render, get_object_or_404
from .models import Products

# 1. Nová úvodní stránka (Domů)
def home(request):
    return render(request, 'exitems/home.html')

# 2. Stránka s výpisem produktů (Katalog)
def products_list(request):
    vsechny_produkty = Products.objects.all() 
    return render(request, 'exitems/products.html', {'produkty': vsechny_produkty})

# 3. O nás
def about(request):
    return render(request, 'exitems/about.html')

# 4. Kontakt
def contact(request):
    return render(request, 'exitems/contact.html')

# 5. Přihlášení / Registrace
def login_view(request):
    return render(request, 'exitems/login.html')

# 6. Detail produktu
def product_detail(request, product_id):
    produkt = get_object_or_404(Products, id=product_id)
    return render(request, 'exitems/detail.html', {'produkt': produkt})
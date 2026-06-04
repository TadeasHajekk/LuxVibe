from django.shortcuts import render, get_object_or_404
from .models import Products, Orders
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

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
# --- PŘIHLAŠOVÁNÍ A REGISTRACE ---

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # Uloží nového uživatele do databáze
            login(request, user)        # Rovnou ho přihlásí
            return redirect('home')     # Přesměruje ho na hlavní stránku
    else:
        form = UserCreationForm()
    
    return render(request, 'exitems/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()      # Získá ověřeného uživatele
            login(request, user)        # Přihlásí ho
            return redirect('home')
    else:
        form = AuthenticationForm()
        
    return render(request, 'exitems/login.html', {'form': form})

def logout_view(request):
    logout(request)                     # Odhlásí uživatele
    return redirect('home')

# 6. Detail produktu
def product_detail(request, product_id):
    produkt = get_object_or_404(Products, id=product_id)
    return render(request, 'exitems/detail.html', {'produkt': produkt})

# --- KOŠÍK ---

@login_required(login_url='/prihlaseni/')
def add_to_cart(request, product_id):
    produkt = get_object_or_404(Products, id=product_id)

    # Zkontrolujeme, jestli už uživatel tento produkt v košíku má
    objednavka, vytvoreno = Orders.objects.get_or_create(
        user=request.user,
        product=produkt,
        defaults={'quantity': 1, 'total_price': produkt.price}
    )

    # Pokud ho už v košíku má, jen mu zvýšíme počet kusů a přepočítáme cenu
    if not vytvoreno:
        objednavka.quantity += 1
        objednavka.total_price += produkt.price
        objednavka.save()

    return redirect('cart')

@login_required(login_url='/prihlaseni/')
def cart_view(request):
    # Vytáhneme z databáze jen ty objednávky (položky), které patří aktuálnímu uživateli
    polozky_v_kosiku = Orders.objects.filter(user=request.user)

    # Spočítáme celkovou hodnotu nákupu
    celkova_cena = sum(polozka.total_price for polozka in polozky_v_kosiku)

    return render(request, 'exitems/cart.html', {
        'polozky': polozky_v_kosiku, 
        'celkova_cena': celkova_cena
    })

@login_required(login_url='/prihlaseni/')
def remove_from_cart(request, order_id):
    # Najdeme konkrétní položku v košíku (Orders) podle jejího ID.
    # Zároveň ověříme, že patří aktuálně přihlášenému uživateli, aby nikdo nemohl mazat cizí košíky.
    polozka = get_object_or_404(Orders, id=order_id, user=request.user)
    
    # Položku smažeme
    polozka.delete()
    
    # Přesměrujeme uživatele zpět do košíku
    return redirect('cart')
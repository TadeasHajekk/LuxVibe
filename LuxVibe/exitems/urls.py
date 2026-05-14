from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                                     # Úvodní stránka
    path('produkty/', views.products_list, name='products'),               # Katalog produktů
    path('o-nas/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),
    path('prihlaseni/', views.login_view, name='login'),
    path('produkt/<int:product_id>/', views.product_detail, name='product_detail'),
]
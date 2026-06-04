from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                                     # Úvodní stránka
    path('produkty/', views.products_list, name='products'),               # Katalog produktů
    path('o-nas/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),
    path('prihlaseni/', views.login_view, name='login'),
    path('produkt/<int:product_id>/', views.product_detail, name='product_detail'),
    path('prihlaseni/', views.login_view, name='login'),
    path('registrace/', views.register_view, name='register'),
    path('odhlaseni/', views.logout_view, name='logout'),
    path('pridat-do-kosiku/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('kosik/', views.cart_view, name='cart'),
    path('odebrat/<int:order_id>/', views.remove_from_cart, name='remove_from_cart'),
]

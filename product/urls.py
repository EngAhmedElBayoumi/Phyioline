from . import views
from django.urls import path

app_name = "product"

urlpatterns = [
    path("", views.product, name="product"),
    path("search", views.search, name="search"),
    path("category_filter/<str:obj>", views.category_filter, name="category_filter"),
    path("shop_details/<str:slug>", views.shop_details, name="shop_details"),
    path("add_to_card/<str:slug>", views.add_to_card, name="add_to_card"),
    path("add_to_card_2/<str:slug>", views.add_to_card_2, name="add_to_card_2"),
    path("remove_from_card/<str:slug>", views.remove_from_card, name="remove_from_card"),
    path("cart", views.cart, name="cart"),
    path("update-cart/", views.update_cart, name="update_cart"),
    path("add_to_wishlist/<str:slug>", views.add_to_wishlist, name="add_to_wishlist"),
    path("add_to_wishlist_2/<str:slug>", views.add_to_wishlist_2, name="add_to_wishlist_2"),
    path("remove_from_wishlist/<str:slug>", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("wishlist", views.wishlist, name="wishlist"),
    path('payment/initiate/', views.initiate_payment, name='initiate_payment'),
    path('payment/complete/', views.payment_complete, name='payment_complete'),
]
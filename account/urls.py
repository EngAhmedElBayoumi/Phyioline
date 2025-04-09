from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("login", views.log_in, name="login"),
    path('logout',views.log_out,name="logout")
]
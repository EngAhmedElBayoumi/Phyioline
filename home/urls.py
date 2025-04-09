from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("terms_conditions", views.terms_conditions, name="terms_conditions"),
    path("refund", views.refund_and_policy_def, name="refund_and_policy_def"),
    path("apply", views.apply, name="apply"),
]
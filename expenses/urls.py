from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("accounts/signup", views.SignUpView.as_view(), name='signup'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("deposit/", views.deposit, name='deposit'),
    path("expense-chart/", views.chart, name='chart'),
    path("new-expense/<int:id>", views.view_all_expenses, name="view_all_expenses"),
    path("new-expense/", views.create, name="create"),
    path("all-expenses/edit/<int:id>", views.edit, name="edit"),
    path("all-expenses/remove/<int:id>", views.remove, name="remove"),
    path("all-expenses/", views.view_all_expenses, name="view_all_expenses"),
    path("", views.home, name="home"),
]
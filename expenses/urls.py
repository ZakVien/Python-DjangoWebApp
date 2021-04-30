from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.deposit, name='deposit'),
    path("chart/", views.chart, name='chart'),
    path("create/<int:id>", views.view_all_expenses, name="view_all_expenses"),
    path("create/", views.create, name="create"),
    path("expenses/edit/<int:id>", views.edit, name="edit"),
    path("expenses/remove/<int:id>", views.remove, name="remove"),
    path("expenses/", views.view_all_expenses, name="view_all_expenses"),
    # path("edit/", views.home, name="home"),
    path("", views.home, name="home"),
]
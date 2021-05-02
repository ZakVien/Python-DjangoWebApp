from django.db import models
from django.conf import settings
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect
from .forms import ExpenseForm, DepositForm
from .models import Expense, Category, Deposit
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

def home(response):
    return render(response, "expenses/index.html", {})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def deposit(response):
    if not response.user.is_authenticated:
        return redirect('login')

    if response.method == "POST":
        form = DepositForm(response.POST)

        if form.is_valid():
            account_id = response.user.id
            date = form.cleaned_data["date"]
            amount = form.cleaned_data["amount"]
            category = form.cleaned_data["category"]
            t = Expense(
                date=date,
                category=category,
                merchant='Deposit',
                amount=amount,
                account=account_id,
            )
            t.save()
            return redirect('view_all_expenses')
        else:
            return render(response, "expenses/deposit.html", {"form": form})
    else:
        form = DepositForm()
    return render(response, "expenses/deposit.html", {"form": form})


def create(response):
    if not response.user.is_authenticated:
        return redirect('login')

    if response.method == "POST":
        form = ExpenseForm(response.POST)

        if form.is_valid():
            account_id = response.user.id
            date = form.cleaned_data["date"]
            category = form.cleaned_data["category"]
            merchant = form.cleaned_data["merchant"]
            amount = form.cleaned_data["amount"]
            t = Expense(
                account=account_id,
                date=date,
                category=category,
                merchant=merchant,
                amount=amount,
            )
            t.save()
            return redirect('view_all_expenses')
        else:
            return render(response, "expenses/create.html", {"form": form})
    else:
        form = ExpenseForm()
    return render(response, "expenses/create.html", {"form": form})


def view_all_expenses(response):
    if not response.user.is_authenticated:
        return redirect('login')

    account_id = response.user.id
    
    order_by = 'date'
    if response.GET.get('order_by'):
        order_by = response.GET.get('order_by')

    ls = Expense.objects.filter(account=account_id).order_by(order_by)

    if ls.count() == 1:
        ls = ls.first()
    return render(response, "expenses/list.html", {"ls": ls})


def edit(response, id):
    if not response.user.is_authenticated:
        return redirect('login')

    ls = Expense.objects.get(id=id)
    update_form = ExpenseForm(instance=ls)

    if response.method == "POST":
        form = ExpenseForm(response.POST, instance=ls)

        if form.is_valid():
            date = form.cleaned_data["date"]
            category = form.cleaned_data["category"]
            merchant = form.cleaned_data["merchant"]
            amount = form.cleaned_data["amount"]

            ls.date = date
            ls.category = category
            ls.merchant = merchant
            ls.amount = amount

            ls.save()
            return HttpResponseRedirect("/expenses/")
        else:
            return render(response, "expenses/edit.html", {"form": form, "ls": ls})

    return render(response, "expenses/edit.html", {"form": update_form, "ls": ls})


def remove(response, id):
    if not response.user.is_authenticated:
        return redirect('login')

    ls = Expense.objects.get(id=id)
    ls.delete()
    return HttpResponseRedirect("/expenses")


def chart(response):
    if not response.user.is_authenticated:
        return redirect('login')

    account_id = response.user.id

    charts = [
        'bar',
        'doughnut',
        'line',
        'pie',
        'polarArea']
    chart_type = 'bar'
    labels = []
    data = []
    merch_select = "checked='checked'"
    ctgry_select = ""
    date_select = ""
    date_range_start = ""
    date_range_end = ""

    if response.method == "POST":
        chart_type = response.POST['chart_type']
        group_by = response.POST['group_by']
        date_range_start = response.POST['date_range_start']
        date_range_end = response.POST['date_range_end']

        if date_range_start == "":
            date_range_start = datetime.datetime.strptime("2070-12-31", '%Y-%m-%d')
            date_range_start = str(date_range_start.date())
        if date_range_end == "":
            date_range_end = datetime.datetime.strptime("1970-12-31", '%Y-%m-%d')
            date_range_end = str(date_range_end.date())

        if group_by == 'category':
            merch_select = ""
            ctgry_select = "checked='checked'"
            date_select = ""
        elif group_by == 'merchant':
            merch_select = "checked='checked'"
            ctgry_select = ""
            date_select = ""
        elif group_by == 'date':
            merch_select = ""
            ctgry_select = ""
            date_select = "checked='checked'"

        if chart_type == 'Polar Area':
            chart_type = 'polarArea'

        # If grouped by category
        if group_by == 'category':
            queryset = Expense.objects.filter(account=account_id).order_by('category')
            # Loop through submitted expenses
            for item in queryset:
                # If category isn't 'Deposit'
                if not item.category_id == 25:
                    # Connect category_id with category name
                    category_query = Category.objects.order_by('category')
                    for category in category_query:
                        # If match, update/add to array
                        if category.id == item.category_id:
                            # If category is already in array, update total
                            if category.category in labels:
                                index = labels.index(category.category)
                                data[index] = str(float(item.amount) + float(data[index]))
                            # Else add new category to array
                            else:
                                start_date = datetime.datetime.strptime(date_range_start, '%Y-%m-%d')
                                end_date = datetime.datetime.strptime(date_range_end, '%Y-%m-%d')
                                if start_date.date() <= item.date <= end_date.date():
                                    labels.append(category.category)
                                    data.append(str(item.amount))
        # If grouped by merchant
        elif group_by == 'merchant':
            queryset = Expense.objects.filter(account=account_id).order_by('merchant')
            # Loop through submitted expenses
            for item in queryset:
                # If category isn't 'Deposit'
                if not item.category_id == 25:
                    # If merchant is already in array, update total
                    if item.merchant in labels:
                        index = labels.index(item.merchant)
                        data[index] = str(round(float(item.amount) + float(data[index]), 2))
                    # Else add new merchant to array
                    else:
                        start_date = datetime.datetime.strptime(date_range_start, '%Y-%m-%d')
                        end_date = datetime.datetime.strptime(date_range_end, '%Y-%m-%d')
                        if start_date.date() <= item.date <= end_date.date():
                            labels.append(item.merchant)
                            data.append(str(item.amount))
        # If grouped by date (default for line graph)
        elif group_by == 'date':
            queryset = Expense.objects.filter(account=account_id).order_by('date')
            # Loop through submitted expenses
            for item in queryset:
                # If category isn't 'Deposit'
                if not item.category_id == 25:
                    # If date is already in array, update total
                    if str(item.date) in labels:
                        index = labels.index(str(item.date))
                        data[index] = str(round(float(item.amount) + float(data[index]), 2))
                    # Else add new date to array
                    else:
                        start_date = datetime.datetime.strptime(date_range_start, '%Y-%m-%d')
                        end_date = datetime.datetime.strptime(date_range_end, '%Y-%m-%d')
                        if start_date.date() <= item.date <= end_date.date():
                            labels.append(str(item.date))
                            data.append(str(item.amount))

    # If not "POST", pass default values
    else:
        queryset = Expense.objects.filter(account=account_id).order_by('merchant')
        # Loop through submitted expenses
        for item in queryset:
            # If category isn't 'Deposit'
            if not item.category_id == 25:
                # Get min and max date values
                if date_range_start == "":
                    date_range_start = datetime.datetime.strptime("2070-12-31", '%Y-%m-%d')
                    date_range_start = date_range_start.date()
                if date_range_end == "":
                    date_range_end = datetime.datetime.strptime("1970-12-31", '%Y-%m-%d')
                    date_range_end = date_range_end.date()
                if item.date <= date_range_start:
                    date_range_start = item.date
                if item.date >= date_range_end:
                    date_range_end = item.date
                # If merchant is already in array, update total
                if item.merchant in labels:
                    index = labels.index(item.merchant)
                    data[index] = str(round(float(item.amount) + float(data[index]), 2))
                # Else add new merchant to array
                else:
                    labels.append(item.merchant)
                    data.append(str(item.amount))
        date_range_start = str(date_range_start)
        date_range_end = str(date_range_end)
    label_size = len(labels)

    return render(response, "chart.html", {
        'charts': charts,
        'chart_type': chart_type,
        'labels': labels,
        'data': data,
        'merch_select': merch_select,
        'ctgry_select': ctgry_select,
        'date_select': date_select,
        'date_range_start': date_range_start,
        'date_range_end': date_range_end,
        'label_size': label_size,
    })


###########################################
###########################################
# CREATE METHODS FOR NECESSARY ############
# CHARTS TO MAKE EACH CHART    ############
# USEFUL                       ############
# EX: LINE GRAPH SHOULD BE     ############
# MONEY OVER TIME AND NOT      ############
# COST PER TRANSACTION         ############
###########################################

# 4/4/21
# Modify data so it accepts deposits for LINE graph ONLY
# Then use JS so when LINE graph is selected,
# radio options for Merchant/Category are not visible.
# (And make sure they're visible if LINE graph IS NOT selected.)
#
# Line graph should show account value at the end of each transaction day
# (If no transactions on 2/3/21, then don't show 2/3/21, duh. (Aka leave as-is)
#

# Add filters to select DATE RANGE



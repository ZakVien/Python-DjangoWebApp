import locale

from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma

from .models import Expense, Category


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'merchant', 'formatted_amount')
    ordering = ('-date',)

    @staticmethod
    def formatted_amount(amt):
        return '$' + intcomma(amt.amount)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    ordering = ('category',)


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, CategoryAdmin)

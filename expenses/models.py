from django.db import models
from django.conf import settings

# Create your models here.


class Deposit(models.Model):
    account = models.IntegerField()
    date = models.DateField('Deposit Date')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        limit_choices_to={'category': 'Deposit'},
        default='----'
    )

    def __str__(self):
        formatted_date = self.date.strftime("%B %d, %Y")
        return str(formatted_date)


class Expense(models.Model):
    account = models.IntegerField()
    date = models.DateField('Transaction Date')
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )
    merchant = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        formatted_date = self.date.strftime("%B %d, %Y")
        return str(formatted_date)


class Category(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        ordering = ['category']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class ExpenseItem(models.Model):
    account = models.IntegerField()
    ExpenseList = models.ForeignKey(Expense, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

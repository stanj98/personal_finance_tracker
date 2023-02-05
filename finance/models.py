from django.db import models
from django.contrib.auth.models import User
import datetime


class Group(models.Model):
    host = models.ForeignKey(User, default = 'Deleted host', on_delete = models.SET_DEFAULT)
    code = models.CharField(max_length = 100)
    name = models.CharField(max_length = 50, default=None)
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class SharedTransaction(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, default = 'Deleted user', on_delete = models.SET_DEFAULT)
    item = models.CharField(max_length = 100)
    account = models.CharField(max_length=25, default = 'card')
    category = models.CharField(max_length = 50)
    amount = models.FloatField()
    content = models.TextField(null = True)
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f'{self.category} - {self.item} - {self.transaction_date.strftime("%Y-%m-%d %H:%M:%S")}'

class Transaction(models.Model):
    payer = models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.CharField(max_length = 100)
    account = models.CharField(max_length=25, default = 'card')
    category = models.CharField(max_length = 50)
    amount = models.FloatField()
    content = models.TextField(null = True)
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f'{self.category} - {self.item} - {self.transaction_date.strftime("%Y-%m-%d %H:%M:%S")}'

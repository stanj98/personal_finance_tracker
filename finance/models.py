from django.db import models
from django.contrib.auth.models import User

class GroupTransaction(models.Model):
    payer = models.ForeignKey(User, default = 'Deleted user', on_delete = models.SET_DEFAULT)
    item = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    amount = models.IntegerField()
    content = models.TextField()
    transaction_date = models.DateTimeField(add_now = True)



class Transaction(models.Model):
    payer = models.ForeignKey(User, default = 'Deleted user', on_delete = models.SET_DEFAULT)
    item = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    amount = models.IntegerField()
    content = models.TextField()
    transaction_date = models.DateTimeField(add_now = True)

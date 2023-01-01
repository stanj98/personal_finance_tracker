from django.contrib import admin
from .models import Transaction, Group, SharedTransaction


admin.site.register(Transaction)
admin.site.register(Group)
admin.site.register(SharedTransaction)

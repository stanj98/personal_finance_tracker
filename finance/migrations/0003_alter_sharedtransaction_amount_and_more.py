# Generated by Django 4.1.4 on 2023-01-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedtransaction',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]

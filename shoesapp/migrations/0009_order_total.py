# Generated by Django 4.1.13 on 2023-12-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoesapp', '0008_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]

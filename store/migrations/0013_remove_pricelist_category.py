# Generated by Django 2.2.15 on 2021-01-10 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_pricelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelist',
            name='category',
        ),
    ]

# Generated by Django 2.2.15 on 2021-01-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_pricelist_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]

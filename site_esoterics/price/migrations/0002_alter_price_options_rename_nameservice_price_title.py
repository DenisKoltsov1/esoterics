# Generated by Django 4.0.6 on 2023-04-29 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name_plural': 'Цены'},
        ),
        migrations.RenameField(
            model_name='price',
            old_name='nameService',
            new_name='title',
        ),
    ]

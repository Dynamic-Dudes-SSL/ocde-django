# Generated by Django 3.2.8 on 2021-10-18 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='color',
            new_name='lang',
        ),
    ]

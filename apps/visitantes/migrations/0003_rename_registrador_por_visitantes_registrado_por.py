# Generated by Django 3.2.7 on 2021-10-05 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_auto_20211004_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitantes',
            old_name='registrador_por',
            new_name='registrado_por',
        ),
    ]
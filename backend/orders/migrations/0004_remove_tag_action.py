# Generated by Django 3.2.6 on 2023-06-19 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_cargotype_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='action',
        ),
    ]

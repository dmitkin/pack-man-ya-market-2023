# Generated by Django 3.2.6 on 2023-06-18 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_cargotype_cargotype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargotype',
            name='tag',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='orders.tag'),
        ),
    ]

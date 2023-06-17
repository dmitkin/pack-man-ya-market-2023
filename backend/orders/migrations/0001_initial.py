# Generated by Django 3.2.6 on 2023-06-15 12:46

import uuid

import django.db.models.deletion
import django_enum.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargotype',
            fields=[
                ('cargotype', models.IntegerField(primary_key=True, serialize=False, verbose_name='Тип груза')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Карготип',
                'verbose_name_plural': 'Карготипы',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('sku', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id товара')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('barcode', models.CharField(max_length=50, verbose_name='Штрихкод')),
                ('image_url', models.URLField(verbose_name='Ссылка на изображение')),
                ('a', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Длина')),
                ('b', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ширина')),
                ('c', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Высота')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id заказа')),
                ('order_number', models.IntegerField(unique=True, verbose_name='Номер заказа')),
                ('status', django_enum.fields.EnumCharField(choices=[('ok', 'Ok'), ('formed', 'Formed'), ('fail', 'Fail'), ('in_progress', 'In Progress'), ('canceled', 'Canceled')], max_length=50, verbose_name='Статус')),
                ('delivery_type', models.CharField(max_length=100, verbose_name='Способ доставки')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('carton_type', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Тип упаковки')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Длина')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ширина')),
                ('height', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Высота')),
                ('display_rf_pack', models.BooleanField(verbose_name='Доступно на складе')),
            ],
            options={
                'verbose_name': 'Упаковка',
                'verbose_name_plural': 'Упаковки',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тэг')),
                ('action', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartontype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.package')),
                ('order_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': 'Упаковка заказа',
                'verbose_name_plural': 'Упаковки заказов',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('order_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.item')),
            ],
            options={
                'verbose_name': 'Товар заказа',
                'verbose_name_plural': 'Товары заказов',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='orders.OrderItem', to='orders.Item', verbose_name='Товары'),
        ),
        migrations.AddField(
            model_name='order',
            name='packages',
            field=models.ManyToManyField(through='orders.OrderPackage', to='orders.Package', verbose_name='Упаковки'),
        ),
        migrations.CreateModel(
            name='ItemCargotypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.item')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cargotype')),
            ],
            options={
                'verbose_name': 'Карготип товара',
                'verbose_name_plural': 'Карготипы товаров',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='types',
            field=models.ManyToManyField(through='orders.ItemCargotypes', to='orders.Cargotype', verbose_name='Карготипы'),
        ),
        migrations.AddField(
            model_name='cargotype',
            name='tag',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cargotypes', to='orders.tag'),
        ),
    ]

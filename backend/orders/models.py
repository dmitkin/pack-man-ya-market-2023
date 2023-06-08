import uuid

from django.db import models
from django_enum import EnumField


class Order(models.Model):
    class Status(models.TextChoices):
        OK = "ok"
        FORMED = "formed"
        FAIL = "fail"
        IN_PROGRESS = "in_progress"

    order_key = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Id заказа",
    )
    # items = models.ManyToManyField(
    #     "Item", related_name="order_items", verbose_name="Товары"
    # )
    packages = models.ManyToManyField(
        "Package", related_name="order_packages", verbose_name="Упаковки"
    )
    status = EnumField(Status, max_length=50, verbose_name="Статус")

    def __str__(self):
        return str(self.order_key)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Item(models.Model):
    sku = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Id товара",
    )
    name = models.CharField(max_length=50, verbose_name="Название товара")
    barcode = models.CharField(max_length=50, verbose_name="Штрихкод")
    image = models.ImageField(
        upload_to="item_images/", verbose_name="Картинка"
    )
    order_key = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    count = models.IntegerField(verbose_name="Количество")
    a = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Длина"
    )
    b = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ширина"
    )
    c = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Высота"
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Вес"
    )
    types = models.ManyToManyField(
        "Cargotype", related_name="item_types", verbose_name="Карготипы"
    )

    def __str__(self):
        return str(self.sku)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Cargotype(models.Model):
    cargotype = models.CharField(
        primary_key=True, max_length=50, verbose_name="Тип груза"
    )
    description = models.CharField(max_length=150, verbose_name="Описание")
    items = models.ManyToManyField(
        Item, related_name="cargo_items", verbose_name="Товары"
    )

    def __str__(self):
        return self.cargotype

    class Meta:
        verbose_name = "Карготип"
        verbose_name_plural = "Карготипы"


class Package(models.Model):
    carton_type = models.CharField(
        primary_key=True, max_length=50, verbose_name="Тип упаковки"
    )
    length = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Длина"
    )
    width = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ширина"
    )
    height = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Высота"
    )
    display_rf_pack = models.BooleanField(verbose_name="Доступно на складе")
    orders = models.ManyToManyField(
        Order, related_name="package_orders", verbose_name="Заказы"
    )

    def __str__(self):
        return self.carton_type

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковки"


class ItemCargotypes(models.Model):
    sku = models.ForeignKey(Item, on_delete=models.CASCADE)
    type = models.ForeignKey(Cargotype, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Карготип товара'
        verbose_name_plural = 'Карготипы товаров'

    def __str__(self):
        return f'{self.sku} {self.type}'


class OrderPackage(models.Model):
    orderkey = models.ForeignKey(Order, on_delete=models.CASCADE)
    cartontype = models.ForeignKey(Package, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Упаковка заказа'
        verbose_name_plural = 'Упаковки заказов'

    def __str__(self):
        return f'{self.orderkey} {self.cartontype}'

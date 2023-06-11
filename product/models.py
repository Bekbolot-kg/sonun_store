from django.db import models


class Customer(models.Model):
    name = models.CharField("Имя: ", max_length=100)
    phone = models.CharField("Номер телефона: ", default="+996", max_length=13)
    email = models.EmailField("Email: ", blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField("Имя продукт: ", max_length=100)
    price = models.PositiveIntegerField("Цена", default=500)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("На ожидание", "На ожидание"),
        ("В пути", "В пути"),
        ("Доставлен", "Доставлен"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status

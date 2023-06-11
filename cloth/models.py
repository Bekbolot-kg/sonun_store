from django.db import models


class CustomerCL(models.Model):
    name = models.CharField("Имя: ", max_length=100)
    phone = models.CharField("Номер телефона: ", default="+996", max_length=13)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField("Имя продукт: ", max_length=100)
    image = models.ImageField('Фото: ', upload_to='')
    price = models.PositiveIntegerField("Цена", default=500)
    size = models.CharField('Размер: ', max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("На ожидание", "На ожидание"),
        ("В пути", "В пути"),
        ("Доставлен", "Доставлен"),
    )

    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status

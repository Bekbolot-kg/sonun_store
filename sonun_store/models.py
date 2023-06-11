from django.db import models


class Sonun_Store(models.Model):
    COLOR = (
        ("Белый", "Белый"),
        ("Черный", "Черный"),
        ("Красный", "Красный"),
        ("Зеленый", "Зеленый"),
        ("Коричневый", "Коричневый"),
        ("Желтый", "Желтый"),
        ("Розовый", "Розовый"),
        ("Синий", "Синий"),
        ("Другое", "Другое"),
    )

    name = models.CharField("Название", max_length=100, null=True)
    image = models.ImageField("Фото", upload_to="", null=True)
    size = models.CharField("Размер", max_length=100, blank=True, null=True)
    color = models.CharField("Цвет", max_length=20, choices=COLOR, null=True)
    price = models.CharField("Цена", max_length=8, null=True)
    brand = models.CharField("Бранд", max_length=100, blank=True, null=True)
    description = models.TextField("Описание", null=True)
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=(("В наличии", "В наличии"), ("Распродано", "Распродано")),
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name_reviews = models.ForeignKey(
        Sonun_Store, on_delete=models.CASCADE, related_name="comment_object", null=True
    )
    text = models.TextField("Ваш отзыв", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

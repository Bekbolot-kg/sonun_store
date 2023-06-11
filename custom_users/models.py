from django.db import models
from django.contrib.auth.models import User

GENDER = (("M", "M"), ("Ж", "Ж"), ("Другой", "Другой"))
LANGUAGE = (
    ("Кыргызча", "Кыргызча"),
    ("Русский", "Русский"),
    ("English", "English"),
)
COUNTY = (
    ("Кыргызстан", "Кыргызстан"),
    ("Россия", "Россия"),
    ("Казахстан", "Казахстан"),
)


class CustomUser(User):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    phone_namber = models.CharField(max_length=14, default="+996777777777")
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=100, choices=GENDER, blank=True, null=True)
    avatar = models.ImageField(upload_to="", null=True)
    language = models.CharField(max_length=50, choices=LANGUAGE, null=True)
    country = models.CharField(max_length=50, choices=COUNTY, blank=True, null=True)
    about_me = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username

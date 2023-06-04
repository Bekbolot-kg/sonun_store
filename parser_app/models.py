from django.db import models

# Create your models here.
class TvParser(models.Model):
    title_url = models.CharField(max_length=200)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title_text

class PrParser(models.Model):
    title_url = models.CharField(max_length=200, null=True)
    title_text = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.title_text
# Generated by Django 4.2.1 on 2023-06-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvparser',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tvparser',
            name='title_url',
            field=models.CharField(max_length=200),
        ),
    ]

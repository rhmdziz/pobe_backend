# Generated by Django 5.0.4 on 2024-06-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0007_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=3000),
        ),
    ]
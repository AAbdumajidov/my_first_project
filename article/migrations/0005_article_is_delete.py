# Generated by Django 4.1.3 on 2022-12-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_category_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='self-product'),
            preserve_default=False,
        ),
    ]

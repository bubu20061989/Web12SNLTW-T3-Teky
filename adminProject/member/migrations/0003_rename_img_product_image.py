# Generated by Django 5.1.1 on 2024-11-05 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_product_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]

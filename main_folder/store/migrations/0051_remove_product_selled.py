# Generated by Django 5.0.7 on 2024-10-16 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0050_rename_selld_product_selled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='selled',
        ),
    ]
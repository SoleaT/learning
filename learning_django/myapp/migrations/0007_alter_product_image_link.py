# Generated by Django 4.2.5 on 2023-10-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_product_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Product_'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-10 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_mainimg_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='mainImg',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='productName',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='productPrice',
        ),
    ]
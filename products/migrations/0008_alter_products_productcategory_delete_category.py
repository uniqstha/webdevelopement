# Generated by Django 4.0.5 on 2022-07-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productCategory',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
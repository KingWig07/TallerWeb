# Generated by Django 5.0.6 on 2024-06-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_detalles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='detalles',
            field=models.CharField(blank=True, max_length=1100, null=True, verbose_name='Detalles del producto'),
        ),
    ]
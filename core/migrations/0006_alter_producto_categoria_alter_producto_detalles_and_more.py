# Generated by Django 5.0.6 on 2024-06-27 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_producto_marca_remove_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='detalles',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='detalles del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto',
            field=models.CharField(max_length=80, verbose_name='nombre del producto'),
        ),
    ]

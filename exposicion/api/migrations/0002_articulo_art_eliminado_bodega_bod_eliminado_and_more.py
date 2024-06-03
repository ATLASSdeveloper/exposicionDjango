# Generated by Django 5.0.6 on 2024-06-03 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='art_eliminado',
            field=models.CharField(default='no', max_length=2),
        ),
        migrations.AddField(
            model_name='bodega',
            name='bod_eliminado',
            field=models.CharField(default='no', max_length=2),
        ),
        migrations.AddField(
            model_name='detallebodega',
            name='det_bod_eliminado',
            field=models.CharField(default='no', max_length=2),
        ),
        migrations.AlterField(
            model_name='detallebodega',
            name='det_bod_art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.articulo'),
        ),
        migrations.AlterField(
            model_name='detallebodega',
            name='det_bod_bod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.bodega'),
        ),
    ]

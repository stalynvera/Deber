# Generated by Django 5.1.3 on 2024-11-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

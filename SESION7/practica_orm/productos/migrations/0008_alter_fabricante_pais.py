# Generated by Django 5.1.4 on 2024-12-31 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_agregacion_de_relacion_y_campos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricante',
            name='pais',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
# Generated by Django 4.1 on 2022-09-11 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api16', '0003_alter_empresa_fecha_creacion_alter_empresa_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, max_length=30, null=True),
        ),
    ]

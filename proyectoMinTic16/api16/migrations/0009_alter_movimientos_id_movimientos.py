# Generated by Django 4.1 on 2022-09-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api16', '0008_alter_movimientos_id_movimientos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='id_movimientos',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

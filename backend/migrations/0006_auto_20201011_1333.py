# Generated by Django 3.1.2 on 2020-10-11 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20201011_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='nom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.nom'),
        ),
    ]

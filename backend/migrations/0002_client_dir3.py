# Generated by Django 3.1.2 on 2020-10-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='dir3',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

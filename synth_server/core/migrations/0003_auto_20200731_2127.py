# Generated by Django 3.0.8 on 2020-07-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200731_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lines',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

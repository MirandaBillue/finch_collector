# Generated by Django 4.1.2 on 2022-10-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_lifestyle_migrates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifestyle',
            name='migrates',
            field=models.BooleanField(),
        ),
    ]

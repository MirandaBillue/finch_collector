# Generated by Django 4.1.2 on 2022-10-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_lifestyle_lifestyle_alter_lifestyle_migrates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifestyle',
            name='migrates',
            field=models.CharField(max_length=20),
        ),
    ]

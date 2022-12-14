# Generated by Django 4.1.2 on 2022-10-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lifestyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifestyle',
            name='lifestyle',
            field=models.CharField(choices=[('T', 'Terrestrial'), ('O', 'Oviparous'), ('A', 'Arboreal'), ('C', 'Congregatory'), ('N', 'Nomadic')], default='T', max_length=150),
        ),
        migrations.AlterField(
            model_name='lifestyle',
            name='migrates',
            field=models.BooleanField(choices=[(1, 'Yes'), (2, 'No')], default=2),
        ),
    ]

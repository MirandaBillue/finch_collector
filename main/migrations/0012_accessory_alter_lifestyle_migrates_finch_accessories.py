# Generated by Django 4.1.2 on 2022-10-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_lifestyle_migrates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='lifestyle',
            name='migrates',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='finch',
            name='accessories',
            field=models.ManyToManyField(to='main.accessory'),
        ),
    ]
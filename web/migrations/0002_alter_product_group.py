# Generated by Django 4.0.4 on 2022-04-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('accessories', 'accessories'), ('mobile', 'mobile'), ('pc', 'pc'), ('notebook', 'notebook')], default='mobile', max_length=20),
        ),
    ]

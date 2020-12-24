# Generated by Django 3.1.3 on 2020-12-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201223_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='Contact',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
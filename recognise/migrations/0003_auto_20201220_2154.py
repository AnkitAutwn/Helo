# Generated by Django 3.1.3 on 2020-12-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognise', '0002_auto_20201220_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='category',
        ),
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
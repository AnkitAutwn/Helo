# Generated by Django 3.1.3 on 2020-12-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_delete_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Image1',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image10',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image2',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image3',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image4',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image5',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image6',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image7',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image8',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Image9',
            field=models.ImageField(null=True, upload_to='people_faces'),
        ),
    ]

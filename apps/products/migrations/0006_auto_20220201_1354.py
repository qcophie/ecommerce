# Generated by Django 3.2.9 on 2022-02-01 13:54

from django.db import migrations, models
import utilities.constants


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220201_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utilities.constants.generate_image_upload_prefix),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
# Generated by Django 3.2.9 on 2022-02-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220201_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='PRODUCT/2022/02/01/13/38/21efe8a5ab589d4a2d96c4ad46ce081e5f/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

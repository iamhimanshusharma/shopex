# Generated by Django 3.0.7 on 2021-08-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210825_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_pic',
            field=models.ImageField(default='profile.png', upload_to='shop/'),
        ),
    ]

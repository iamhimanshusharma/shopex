# Generated by Django 3.0.7 on 2021-08-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_email', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 3.2.12 on 2022-09-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0030_alter_register_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', upload_to='images'),
        ),
    ]

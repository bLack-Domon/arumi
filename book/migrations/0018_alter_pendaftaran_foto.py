# Generated by Django 3.2.12 on 2022-08-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_pendaftaran_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendaftaran',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]

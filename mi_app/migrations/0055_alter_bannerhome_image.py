# Generated by Django 5.1.3 on 2024-12-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0054_bannerhome_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerhome',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
    ]
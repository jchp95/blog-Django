# Generated by Django 5.1.2 on 2024-11-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0039_remove_cursos_cursos_list_cursos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='image',
        ),
        migrations.AddField(
            model_name='cursos',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='cursos_list/videos/'),
        ),
    ]
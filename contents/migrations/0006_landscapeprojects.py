# Generated by Django 5.2 on 2025-05-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandscapeProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landscape_project_img', models.ImageField(upload_to='projects_img/')),
            ],
        ),
    ]

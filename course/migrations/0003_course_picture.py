# Generated by Django 2.1.5 on 2019-02-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/course/pictures'),
        ),
    ]
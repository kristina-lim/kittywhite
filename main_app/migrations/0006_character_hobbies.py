# Generated by Django 4.1.3 on 2023-01-12 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_hobby_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='hobbies',
            field=models.ManyToManyField(to='main_app.hobby'),
        ),
    ]
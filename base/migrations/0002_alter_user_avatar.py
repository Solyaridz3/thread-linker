# Generated by Django 4.0 on 2022-01-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar-default-icon_t7p54m', null=True, upload_to=''),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_setofshots', '0040_alter_event_start_alter_post_pub_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='description',
            field=models.TextField(max_length=1024, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(max_length=1024, verbose_name='Описание'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_setofshots', '0010_alter_post_bar_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, help_text='Можно оставить пустым', max_length=64, unique=True, verbose_name='Ссылка'),
        ),
    ]

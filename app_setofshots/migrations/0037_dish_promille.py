# Generated by Django 5.1.1 on 2024-09-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_setofshots', '0036_category_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='promille',
            field=models.IntegerField(blank=True, help_text='Если не алкоголь- оставить пустым', null=True, verbose_name='Крепость'),
        ),
    ]

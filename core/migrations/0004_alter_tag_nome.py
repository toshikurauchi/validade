# Generated by Django 4.2.16 on 2024-11-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tag_cor_fundo_tag_cor_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='nome',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]

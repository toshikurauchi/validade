# Generated by Django 4.2.16 on 2024-11-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag_produto_congelado_produto_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='cor_fundo',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='tag',
            name='cor_texto',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_produto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]

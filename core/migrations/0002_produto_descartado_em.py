# Generated by Django 4.2.16 on 2024-11-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descartado_em',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='created_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='results',
            name='deleted_time',
            field=models.DateTimeField(),
        ),
    ]

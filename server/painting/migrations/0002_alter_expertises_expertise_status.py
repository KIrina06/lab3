# Generated by Django 4.2.4 on 2023-12-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertises',
            name='expertise_status',
            field=models.IntegerField(choices=[(1, 'Действует'), (2, 'Удалена')], default=1),
        ),
    ]

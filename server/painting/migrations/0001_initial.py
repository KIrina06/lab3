# Generated by Django 4.2.4 on 2023-12-13 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expertises',
            fields=[
                ('expertise_id', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.CharField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=70, null=True, unique=True)),
                ('price', models.CharField(blank=True, null=True)),
                ('context', models.CharField(blank=True, null=True)),
                ('expertise_status', models.IntegerField(choices=[(1, 'Действует'), (2, 'Удалена')], default=1, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True)),
                ('login', models.CharField(blank=True, null=True, unique=True)),
                ('password', models.CharField(blank=True, null=True)),
                ('contacts', models.CharField(blank=True, null=True)),
                ('admin_pass', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('request_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('formated_date', models.DateTimeField(blank=True, null=True)),
                ('request_status', models.IntegerField(choices=[(1, 'Черновик'), (2, 'В работе'), (3, 'Завершен'), (4, 'Отклонен'), (5, 'Удален')], default=1)),
                ('moder_id', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='painting.users')),
            ],
        ),
        migrations.CreateModel(
            name='ReqExps',
            fields=[
                ('re_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='painting.expertises')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='painting.requests')),
            ],
            options={
                'unique_together': {('expertise', 'request')},
            },
        ),
    ]

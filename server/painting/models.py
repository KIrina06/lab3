from django.db import models

class Expertises(models.Model):
    STATUS_CHOICES = (
        (1, 'Действует'),
        (2, 'Удалена'),
    )

    expertise_id = models.AutoField(primary_key=True)
    picture = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=70, unique=True)
    price = models.CharField(blank=True, null=True)
    context = models.CharField(blank=True, null=True)
    expertise_status = models.IntegerField(choices=STATUS_CHOICES, default=1)

class Requests(models.Model):
    STATUS_CHOICES = (
        (1, 'Черновик'),
        (2, 'В работе'),
        (3, 'Завершен'),
        (4, 'Отклонен'),
        (5, 'Удален'),
    )

    request_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    expertises = models.ManyToManyField(Expertises)
    closed_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    formated_date = models.DateTimeField(blank=True, null=True)
    req_status = models.IntegerField(choices=STATUS_CHOICES, default=1)  # This field type is a guess.
    moder_id = models.IntegerField(blank=True, null=True)


class ReqExps(models.Model):
    re_id = models.BigAutoField(primary_key=True)
    expertise = models.ForeignKey('Expertises', models.DO_NOTHING)
    request = models.ForeignKey('Requests', models.DO_NOTHING)

    class Meta:
        unique_together = (('expertise', 'request'),)

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    login = models.CharField(blank=True, null=True, unique=True)
    password = models.CharField(blank=True, null=True)
    contacts = models.CharField(blank=True, null=True)
    admin_pass = models.BooleanField(blank=True, null=True, default=False)
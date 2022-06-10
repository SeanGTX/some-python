from django.db import models


class Girl(models.Model):
    girl_count = models.IntegerField('Номер')
    girl_name = models.CharField('Имя и фамилия', max_length=50)

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self)->str:
        return f'Account:{self.user.id}/{self.full_name}'

    class Meta:
        ordering=(
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name = 'Аккаунты'
class Group(models.Model):
    GROUP_NAME_MAX_LENGHT = 10

    name = models.CharField(
        max_length = GROUP_NAME_MAX_LENGHT
    )
    def _str__(self)->str:
        return 'Группы (self.name)'
    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name = 'Группы'
class Student(models.Model):

    accaunt = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )
    age = models.IntegerField(
        'Возраст студента'
    )
    gpa = models.FloatField(
        'Средний балл'
    )
    group =models.ForeignKey(
        Group,
        on_delete=models.PROTECT
    )
    def __str__(self)->str:
        return f'Возраст : {self.age}/n Группа {self.gpa}/n Оценка {self.group}'
    class Meta:
        ordering=('accaunt',)
        verbose_name = 'Студент'
        verbose_name = 'Студенты'
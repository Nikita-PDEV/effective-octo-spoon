from django.db import models

class PassUser(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')
    firstname = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    lastname = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    surname = models.CharField(max_length=30, blank=True, verbose_name='Отчество')

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
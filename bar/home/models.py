from django.contrib.auth.models import User
from django.db import models


class servis(models.Model):
    img = models.ImageField(upload_to="images/", verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Название услуги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class logo(models.Model):
    img = models.ImageField(upload_to="images/", verbose_name='Логотип (фото)')

    class Meta:
        verbose_name = "Логотип"
        verbose_name_plural = "Логотипы"


class barber(models.Model):
    img = models.ImageField(upload_to="images/", verbose_name='Фото')
    title = models.CharField(max_length=64, verbose_name='Имя мастера')
    description = models.TextField(verbose_name='Информация о мастере')
    phone = models.CharField(max_length=17, verbose_name='Телефон мастера')
    service = models.ForeignKey(servis, on_delete=models.CASCADE, related_name="barber_servis", verbose_name="Услуга")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class comment(models.Model):
    barber = models.ForeignKey(barber, on_delete=models.CASCADE, related_name='comment_barber', verbose_name='Мастер')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-id']


class work(models.Model):
    img = models.ImageField(upload_to="images/", verbose_name='Фото')
    barber = models.ForeignKey(barber, on_delete=models.CASCADE, related_name='work_barber', verbose_name='Мастер')

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'




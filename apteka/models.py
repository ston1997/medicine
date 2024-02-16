from django.db import models


class Medicament(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    price = models.FloatField('Цена')

    class Meta:
        verbose_name = "Медикамент"
        verbose_name_plural = "Медикаменты"

    def __str__(self):
        return self.name


class Salesman(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self):
        return self.surname


class Check(models.Model):
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE, verbose_name='Продавец', related_name='checks')
    date_at = models.DateTimeField('Дата продажи', auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.pk)


class PositionCheck(models.Model):
    sale = models.ForeignKey(Check, on_delete=models.CASCADE, verbose_name='Номер заказа', related_name='positions')
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, verbose_name='Название')
    count = models.PositiveIntegerField('Количество')

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"

    def __str__(self):
        return self.medicament.name

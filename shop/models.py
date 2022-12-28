from django.db import models

class Shop(models.Model):
    title = models.CharField('Заголовок', max_length=125)
    body = models.TextField('Контент')
    price = models.CharField('Цена', max_length=100, blank=True)
    date = models.DateField('Дата')

    img1 = models.ImageField('Фотография', upload_to='static/media/')
    img3 = models.ImageField('Фотография', upload_to='static/media/')
    img2 = models.ImageField('Фотография', upload_to='static/media/')

    rubric = models.ForeignKey('Rubrics', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = '-title',


class Rubrics(models.Model):
    name = models.CharField('Рубрика', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
from django.db import models

# Create your models here.
class YandexMapsQ(models.Model):
    """
    БД запросов к нашему API
    """
    user = models.IntegerField(verbose_name='ID пользователя из БД backend-а',
                                blank=True, null=True)
    tguser = models.IntegerField(verbose_name='ID пользователя из Telegram-а',
                                blank=True, null=True)
    query_str = models.CharField(max_length=500, verbose_name='Введенная строка пользователем. Ожидается - адрес')
    link_to_ya_map = models.TextField(verbose_name='Ссылка на Яндекс.Карты')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания/редактирования записи в БД')

    def __str__(self):
        return "%s" % (self.query_str)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросов'


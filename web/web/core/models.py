import datetime
from django.db import models
from django.utils import timezone


class ObjectManager(models.Manager):
    def get_queryset(self):
        return super(ObjectManager, self).get_queryset().all()


class Faq(models.Model):

    """ Модель справки."""

    objects = ObjectManager()

    title = models.CharField(verbose_name='Тема', max_length=128)
    description = models.TextField(verbose_name='Содержание', max_length=255)

    class Meta:
        ordering = ['title']
        verbose_name = 'Справка'
        verbose_name_plural = 'Справки'
        unique_together = ['title', 'description' ]

    def __str__(self):
        return self.title


class Member(models.Model):
    """
    Модель пользователя канала
    Переопределенный метод save() проверяет содержимое username и, при пустом значении, заполняет его
    из поля user_id
    """

    objects = ObjectManager()

    user_id = models.CharField(verbose_name='id', max_length=128, unique=True)
    username = models.CharField(verbose_name='Ник', max_length=128, null=True, blank=True)
    name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    role = models.CharField(verbose_name='Роль в канале', max_length=128, null=True, blank=True)
    violation = models.IntegerField(verbose_name='Количество нарушений', default=0)

    class Meta:
        ordering = ['user_id', 'username']
        verbose_name = 'Мембер'
        verbose_name_plural = 'Мемберы'

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        if self.username is None:  # and self.name is None:
            if self.name is None:
                self.username = self.user_id
            else:
                self.username = self.name
        super(Member, self).save(*args, **kwargs)


class Block(models.Model):
    """
    Модель блокировки юзверя
    Переопределенный save() при использовании добавляет Member'у одно нарушение и высчитывает время
    снятия бана. Если поле permanent модели = True, бан выдается до 9999-го года =Р
    В противном случае высчитывается время в зависимости от количества нарушений пользователя
    """

    objects = ObjectManager()

    user = models.CharField(verbose_name='Мембер', max_length=128)
    start_time = models.DateTimeField(verbose_name='Время начала', default=timezone.now)
    stop_time = models.DateTimeField(verbose_name='Время окончания')
    permanent = models.BooleanField(verbose_name='Бан перманентно', default=False)

    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Блокировка'
        verbose_name_plural = 'Блокировки'

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        u = Member.objects.get(username=self.user)
        u.violation += 1
        u.save()
        if self.permanent:
            self.stop_time = datetime.datetime(9999, 12, 1, 12, 00, 00)
        else:
            block_time = u.violation * 10 + (u.violation - 1) * 10
            self.stop_time = timezone.now() + timezone.timedelta(minutes=block_time)
        super(Block, self).save(*args, **kwargs)

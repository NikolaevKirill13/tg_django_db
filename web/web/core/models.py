from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager, AbstractUser
import datetime

class ObjectManager(models.Manager):
    def get_queryset(self):
        return super(ObjectManager, self).get_queryset().all()


class User(AbstractUser):

    """Модель пользователя"""

    objects = UserManager()

    user_id_tg = models.IntegerField(verbose_name='Id пользователя в telegram', unique=True, null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    warn = models.IntegerField(verbose_name='', default=0, null=True, blank=True)

    class Meta:
        ordering = ['username']
        verbose_name = 'Мембер'
        verbose_name_plural = 'Мемберы'

    def __str__(self):
        return self.username


class Faq(models.Model):

    """ Модель справки."""

    objects = ObjectManager()

    title = models.CharField(verbose_name='Тема', max_length=128, unique=True)
    description = models.TextField(verbose_name='Содержание', max_length=255)

    class Meta:
        ordering = ['title']
        verbose_name = 'Справка'
        verbose_name_plural = 'Справки'

    def __str__(self):
        return self.title


class Block(models.Model):
    """
    Модель блокировки юзверя
    Переопределенный save() при использовании добавляет Member'у одно нарушение и высчитывает время
    снятия бана. Если поле permanent модели = True, бан выдается до 9999-го года =Р
    В противном случае высчитывается время в зависимости от количества нарушений пользователя
    """

    objects = ObjectManager()

    user = models.CharField(verbose_name='Мембер', max_length=128)
    start_time = models.DateTimeField(verbose_name='Время начала', default=timezone.now, null=True, blank=True)  # время понадобится в
    # будущем развитии
    stop_time = models.DateTimeField(verbose_name='Время окончания', null=True, blank=True)
    permanent = models.BooleanField(verbose_name='Бан перманентно', default=False, null=True, blank=True)
    warn = models.IntegerField(verbose_name='Нарушение', default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'Блокировка'
        verbose_name_plural = 'Блокировки'

    def __str__(self):
        return self.user_id

    def save(self, *args, **kwargs):
        user = User.objects.get(user_id_tg=self.user)
        user.warn += 1
        user.save()
        self.warn = user.warn
        if self.permanent:
            self.stop_time = datetime.datetime(9999, 12, 1, 12, 00, 00)
        else:
            block_time = user.warn * 10 + (user.warn - 1) * 10
            self.stop_time = timezone.now() + timezone.timedelta(minutes=block_time)
        super(Block, self).save(*args, **kwargs)

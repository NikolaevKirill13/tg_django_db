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

    def __str__(self):
        return self.title


class Member(models.Model):
    """
    Модель пользователя канала
    Переопределенный метод save() проверяет содержимое username и, при пустом значении, заполняет его
    из поля user_id
    """

    objects = ObjectManager()

    user_id = models.IntegerField(verbose_name='user_id', max_length=128, unique=True, null=False)
    username = models.CharField(verbose_name='Ник', max_length=128, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    full_name = models.CharField(verbose_name='Фамилия и имя', max_length=255, null=True, blank=True)
    role = models.CharField(verbose_name='Роль в канале', max_length=128, null=True, blank=True)

    class Meta:
        ordering = ['user_id', 'username', 'full_name']
        verbose_name = 'Мембер'
        verbose_name_plural = 'Мемберы'

    def __str__(self):
        return f'{self.user_id}'

    def save(self, *args, **kwargs):
        if self.username is None:  # and self.name is None:
            self.username = self.user_id
        super(Member, self).save(*args, **kwargs)


class Block(models.Model):
    """
    Модель блокировки юзверя
    Переопределенный save() при использовании добавляет Member'у одно нарушение и высчитывает время
    снятия бана. Если поле permanent модели = True, бан выдается до 9999-го года =Р
    В противном случае высчитывается время в зависимости от количества нарушений пользователя
    """

    objects = ObjectManager()

    user_id = models.BigIntegerField(verbose_name='Мембер', unique=True)
    warn = models.PositiveIntegerField(verbose_name='Нарушений', default=0)

    class Meta:
        verbose_name = 'Блокировка'
        verbose_name_plural = 'Блокировки'

    def __str__(self):
        return self.user_id

    # def save(self, *args, **kwargs):
    #     u = Member.objects.get(user_id=self.user_id)
    #     u.save()
    #     super(Block, self).save(*args, **kwargs)
    # Не уверен что это нужно тк у нас в таблице block будут и user_id и количество нарушений
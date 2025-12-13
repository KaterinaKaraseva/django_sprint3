"""Модель."""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Location(models.Model):
    """Модель."""

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Название места'
    )

    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        verbose_name='Добавлено'
    )

    class Meta:
        """Модель."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Category(models.Model):
    """Модель."""

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        blank=False,
        verbose_name='Описание'
    )

    slug = models.SlugField(
        unique=True,
        blank=False,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
    )

    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        verbose_name='Добавлено'
    )

    class Meta:
        """Модель."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Модель."""

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Добавлено'
    )

    text = models.TextField(
        blank=False,
        verbose_name='Текст'
    )

    pub_date = models.DateTimeField(
        blank=False,
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        )
    )

    author = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )

    location = models.ForeignKey(
        Location,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение'
    )

    category = models.ForeignKey(
        Category,
        blank=False,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        blank=False,
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        """Модель."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

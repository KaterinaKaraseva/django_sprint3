"""Модели."""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PublishedModel(models.Model):
    """Абстрактная модель с общими полями."""

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
        """Метаданные для абстрактной модели."""

        abstract = True


class Location(PublishedModel):
    """Модель местоположения."""

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Название места'
    )

    class Meta:
        """Метаданные для модели Location."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """Строковое представление объекта Location."""
        return self.name


class Category(PublishedModel):
    """Модель категории."""

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
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        """Метаданные для модели Category."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Строковое представление объекта Category."""
        return self.title


class Post(PublishedModel):
    """Модель публикации."""

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Заголовок'
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
        verbose_name='Автор публикации',
        related_name='posts'
    )

    location = models.ForeignKey(
        Location,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
        related_name='posts'
    )

    category = models.ForeignKey(
        Category,
        blank=False,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts'
    )

    class Meta:
        """Метаданные для модели Post."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        """Строковое представление объекта Post."""
        return self.title

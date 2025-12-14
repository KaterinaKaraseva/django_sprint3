"""Админ-панель для моделей блога."""
from django.contrib import admin
from .models import Category, Post, Location


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админ-панель для модели Category."""
    
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админ-панель для модели Post."""
    
    list_display = ('title', 'pub_date', 'author', 'category', 
                    'location', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'pub_date', 'author')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    date_hierarchy = 'pub_date'
    filter_horizontal = ()
    raw_id_fields = ('author',)
    ordering = ('-pub_date',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Админ-панель для модели Location."""
    
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)
    list_editable = ('is_published',)
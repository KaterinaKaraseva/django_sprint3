from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Category


def get_published_posts():
    """Функция для получения опубликованных постов."""
    current_time = timezone.now()
    return (
        Post.objects
        .select_related('category', 'location', 'author')
        .filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=current_time
        )
    )


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    
    post_list = get_published_posts()[:5]
    context = {
        'post_list': post_list,
    }
    
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категории."""
    template = 'blog/category.html'
    
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    
    current_time = timezone.now()
    post_list = (
        get_published_posts()
        .filter(category=category)
        .order_by('-pub_date')
    )
    
    context = {
        'category': category,
        'post_list': post_list,
    }
    
    return render(request, template, context)


def post_detail(request, pk):
    """Страница отдельной публикации."""
    template = 'blog/detail.html'
    
    current_time = timezone.now()
    post = get_object_or_404(
        get_published_posts(),
        pk=pk
    )
    
    context = {
        'post': post,
    }
    
    return render(request, template, context)
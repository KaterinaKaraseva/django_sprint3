from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils import timezone
from blog.models import Post

current_time = timezone.now()


def index(request):
    """Модель."""
    template = 'blog/index.html'

    post_list = (
        Post.objects
        .select_related('category', 'location', 'author')
        .filter(is_published=True, category__is_published=True,
                pub_date__lte=current_time)
        .order_by('-pub_date')[0:5]
    )
    context = {
        'post_list': post_list,
    }

    return render(request, template, context)


def category_posts(request, category_slug):
    """Модель."""
    template = 'blog/category.html'

    post_list = get_list_or_404(
        Post.objects
        .select_related('category', 'location', 'author')
        .filter(is_published=True, pub_date__lte=current_time,
                category__slug=category_slug, category__is_published=True)
    )

    context = {
        'post_list': post_list,
    }

    return render(request, template, context)


def post_detail(request, pk):
    """Модель."""
    template = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects
        .select_related('category', 'location', 'author'),
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True,
        pk=pk
    )

    context = {
        'post': post,
    }

    return render(request, template, context)

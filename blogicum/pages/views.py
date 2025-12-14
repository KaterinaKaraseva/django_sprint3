"""Представления статических страниц."""
from django.shortcuts import render


def about(request):
    """Страница "О проекте"."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Страница с правилами сайта."""
    template = 'pages/rules.html'
    return render(request, template)
from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


def csrf_failure(request, reason=''):
    template = 'pages/403csrf.html'
    return render(request, template, status=403)


def page_not_found(request, exception):
    template = 'pages/404.html'
    return render(request, template, status=404)


def internal_server_error(request):
    template = 'pages/500.html'
    return render(request, template, status=500)

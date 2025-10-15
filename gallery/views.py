from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    """Displays home page"""
    template_name = 'index.html'


class AboutPage(TemplateView):
    """Displays the About page with artist bio, philosophy and process"""
    template_name = 'about.html'

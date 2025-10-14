from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

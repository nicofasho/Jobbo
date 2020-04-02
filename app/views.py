"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import Scrape

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    scrapes = Scrape.objects.all()

    return render(
        request,
        'app/index.html',
        {
            'title': 'Recent Scrapes - Jobbo',
            'year': datetime.now().year,
            'scrapes': scrapes
        }
    )

class ScrapeDetail(DetailView):
    model = Scrape

    def get_context_data(self, **kwargs):
        obj = super().get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = obj
        context['year'] = datetime.now().year
        return context

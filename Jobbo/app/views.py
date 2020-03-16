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
    paginator = Paginator(scrapes, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'app/index.html',
        {
            'title': 'Recent Scrapes - Jobbo',
            'year': datetime.now().year,
            'page_obj': page_obj
        }
    )

class ScrapeDetail(DetailView):
    model = Scrape

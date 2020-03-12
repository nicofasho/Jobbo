"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Scrape

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Recent Scrapes',
            'year':datetime.now().year,
        }
    )

def detail(request, scrape_id):
    # Renders Scrape Detail page
    assert isinstance(request, HttpRequest)
    curr_scrape = Scrape.objects.get(id=scrape_id)
    return render(
        request,
        'app/detail.html',
        {
            'title': f'Jobs Found on {curr_scrape.run_time}',
            'scrape': curr_scrape,
            'year':datetime.now().year
        })
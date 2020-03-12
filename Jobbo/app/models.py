"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from django.utils import timezone
from . import scraper

from django.db.models.signals import post_save
from django.dispatch import receiver


class Scrape(models.Model):
    run_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['run_time']
    
    def __str__(self):
        return f'Jobs scraped on {self.run_time}'

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    date_posted = models.DateTimeField()
    day_scraped = models.ForeignKey(Scrape, on_delete=models.CASCADE)
    logo_url = models.CharField(max_length=300, blank=True)
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Scrape)
def scrape_and_format(sender, instance, created, **kwargs):
    if created:
        remote_ok_jobs = scraper.scrape_remoteok()
        wework_jobs = scraper.scrape_weworkremotely()

        for job in wework_jobs:
            Job.objects.get_or_create(
                day_scraped=instance,
                title=job['title'],
                company=job['company'],
                url=job['url'],
                date_posted=job['posted'],
                logo_url=job['logo_url'],
                source=job['source']
                )

        for job in remote_ok_jobs:
            Job.objects.get_or_create(
                day_scraped=instance,
                title=job['title'],
                company=job['company'],
                url=job['url'],
                date_posted=job['posted'],
                logo_url=job['logo_url'],
                source=job['source']
                )
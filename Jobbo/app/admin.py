from django.contrib import admin
from .models import Scrape, Job

class JobInline(admin.StackedInline):
    model = Job

class ScrapeAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['run_time']})
        ]
    inlines = [JobInline]

admin.site.register(Scrape, ScrapeAdmin)

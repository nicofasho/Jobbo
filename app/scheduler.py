
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Scrape, Job


def new_scrape():
    s = Scrape()
    s.save()

def start_background_job():
    print('starting scheduler...')
    scheduler = BackgroundScheduler()
    scheduler.add_job(new_scrape, 'cron', day_of_week='mon', hour=9, minute=0)
    scheduler.start()
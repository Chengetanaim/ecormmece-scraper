from .adding import process
from apscheduler.schedulers.background import BackgroundScheduler


def product_start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process, 'interval', hours=24)
    scheduler.start()
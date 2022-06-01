from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from snippets.ModelUtils import *

def start():
    scheduler = BackgroundScheduler(misfire_grace_time=5, coalesce=True)
    scheduler.add_job(ManageTaskSchedule,'interval', seconds=5)
    #scheduler.add_job(ManageTaskSchedule,'cron',hour=23,minute=59,second=59)
    scheduler.start()

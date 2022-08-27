from calendar import month
from apscheduler.schedulers.blocking import BlockingScheduler

from termin import termin_alert

sched = BlockingScheduler()

@sched.scheduled_job('cron', month='5-9', second='*/30')
def timed_job():
    termin_alert()

if __name__ == "__main__":
    sched.start()
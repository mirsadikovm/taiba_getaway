from celery import shared_task
from datetime import datetime, timezone
import pytz
from worker.models import EmployeeTimout


@shared_task
def emp_timeout():
    timeout = datetime.now(tz=timezone.utc)
    for emp in EmployeeTimout.objects.all():
        timedelta = timeout - emp.datetime 
        if timedelta.total_seconds()//3600 >= 2: # type: ignore
            emp.delete()

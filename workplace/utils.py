import json
import requests
from django.conf import settings
from worker.models import EmployeeTimout

def check_employee_exists_by_hash(hashed_data):

    timeout_emp = EmployeeTimout.objects.filter(hash=hashed_data)
    if timeout_emp.exists():
        emp = timeout_emp.first()
        employee=requests.get(f"{settings.REST_FRAMEWORK_URL}/employee/all/{emp.employee_uid}").text # type: ignore
        if employee:
            employee = json.loads(employee)
        return employee
    return False


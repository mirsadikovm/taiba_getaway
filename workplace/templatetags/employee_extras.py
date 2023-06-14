from django import template

from workplace.utils import check_employee_exists_by_hash

register = template.Library()



@register.filter(name="check_employee")
def check_employee(hash_data):
    employee = check_employee_exists_by_hash(hash_data)
    
    return employee.get('uid')  # type: ignore
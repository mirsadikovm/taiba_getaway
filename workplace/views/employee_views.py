import json
import requests
import logging

from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse

from workplace.utils import check_employee_exists_by_hash
from workplace.forms.employee_forms import EmployeeRegisterForm

# Create your views here.

def home(request, hash_data = None):
    emp = check_employee_exists_by_hash(hash_data)
    if emp:
        if emp.get('profession') in ["Директор","Управляющий"]:
            event_lst= json.loads(requests.get(f"{settings.REST_FRAMEWORK_URL}/event/all/").text)
            return render(request,'home.html', context={'emp': emp, 'emp_data': hash_data, 'event_lst': event_lst})
        else:
            return redirect('trucks', hash_data=hash_data)
    return redirect('login')


def get_employee_list(request, hash_data = None):
    
    emp = check_employee_exists_by_hash(hash_data)
    if emp:
            if emp.get('profession') in ["Директор","Управляющий"]:
                form = EmployeeRegisterForm()
                emp_lst= json.loads(requests.get(f"{settings.REST_FRAMEWORK_URL}/employee/all/").text)
                return render(request ,'employee.html', context={'result': emp_lst , 'emp_data': hash_data , 'form' : form , 'emp_profession': emp.get('profession')})
            else:
                return redirect('trucks', hash_data=hash_data)
    return redirect('login')

def create_employee(request, hash_data = None):

    if request.method == "POST":
        data = json.dumps(request.POST.dict())
        headers = {
        'Content-type':'application/json', 
        'Accept':'application/json'
        }
        requests.post(f"{settings.REST_FRAMEWORK_URL}/employee/all/", data=data, headers=headers)
    return HttpResponseRedirect(reverse('employee', kwargs={"hash_data":hash_data}))
        

def delete_employee(request, pk):
 
    logging.warning('Came for delete!')
    requests.delete(f'{settings.REST_FRAMEWORK_URL}/employee/all/{pk}')
    response = {
        'data' : 'User deleted',
    }
    return  JsonResponse(response)
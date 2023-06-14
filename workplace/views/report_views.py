import json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from workplace.utils import check_employee_exists_by_hash
from workplace.forms.truck_forms import TruckForm
# Create your views here.

def get_report_list(request, hash_data = 0):
    
    if check_employee_exists_by_hash(hash_data):
        if request.method == 'POST':
           pass
        else:
            form = TruckForm()
            truck_lst= json.loads(requests.get(f"{settings.REST_FRAMEWORK_URL}/report/all/").text)
            return render(request ,'reports.html', context={'result': truck_lst , 'emp_data': hash_data, 'form': form}) # type: ignore
    return redirect('login')


def create_truck(request, hash_data = None):

    if request.method == "POST":
        data = json.dumps(request.POST.dict())
        headers = {
        'Content-type':'application/json', 
        'Accept':'application/json'
        }
        requests.post(f"{settings.REST_FRAMEWORK_URL}/employee/all/", data=data, headers=headers)
    return HttpResponseRedirect(reverse('employee', kwargs={"hash_data":hash_data}))
        

def delete_truck(request, pk):


    requests.delete(f'{settings.REST_FRAMEWORK_URL}/employee/all/{pk}')
    response = {
        'data' : 'User deleted',
    }
    return  JsonResponse(response)

import json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from workplace.utils import check_employee_exists_by_hash
from workplace.forms.truck_forms import TruckForm
# Create your views here.

def get_trucks_list(request, hash_data = 0):
    
    emp = check_employee_exists_by_hash(hash_data)
    if emp:
            form = TruckForm()
            truck_lst= json.loads(requests.get(f"{settings.REST_FRAMEWORK_URL}/trucks/all/").text)
            return render(request ,'trucks.html', context={'result': truck_lst , 'emp_data': hash_data, 'form': form})
    return redirect('login')


def create_truck(request, hash_data = None):

    if request.method == "POST":
        form = TruckForm(request.POST)
        if form.is_valid():
            request_data = {'driver' : {"frist_name": form.data['frist_name'], "last_name": form.data['last_name'], 'phone_number': form.data['phone_number']},
            "car_number" : form.data["car_number"],
            'city_from' : form.data['city_from'],
            "weight_in_kg": form.data['weight_in_kg'],
            "product_type": "Мясо",
            'arrival_timedate': form.data['arrival_timedate']
            }
            headers = {
            'Content-type':'application/json', 
            'Accept':'application/json'
            }
            requests.post(f"{settings.REST_FRAMEWORK_URL}/trucks/all/", data=json.dumps(request_data), headers=headers)
    return HttpResponseRedirect(reverse('trucks', kwargs={"hash_data":hash_data}))
        

def confirm_truck(request,hashed_data,pk):
    
    emp = check_employee_exists_by_hash(hashed_data)
    data = {"accept_by": emp.get('uid'), "status": "Доставлено"} # type: ignore
    requests.patch(f'{settings.REST_FRAMEWORK_URL}/trucks/all/{pk}/', data = data)
    response = {
        'data' : 'User deleted',
    }
    return  JsonResponse(response)
import json
import requests as r
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponseRedirect

from worker.forms import LoginForm
from worker.models import EmployeeTimout
from worker.utils import get_random_string


# Create your views here.
def log_user_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            employee = r.get(f"{settings.REST_FRAMEWORK_URL}/employee/get/?uid={form['uid'].data}&password={form['password'].data}").text
            if not employee == '[]': 
                employee = json.loads(employee)[0]
                random_data = get_random_string()
                datetime = timezone.now()
                EmployeeTimout.objects.update_or_create(employee_uid = employee.get('uid'), defaults ={'hash': random_data, 'datetime': datetime})
                return HttpResponseRedirect(reverse('main_1', kwargs={"hash_data":random_data}))
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})
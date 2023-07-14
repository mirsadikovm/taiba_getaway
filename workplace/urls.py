from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from workplace.views.employee_views import home, get_employee_list, create_employee, delete_employee
from workplace.views.truck_views import get_trucks_list, create_truck, confirm_truck
from workplace.views.report_views import get_report_list
from workplace.views.time_views import server_time
urlpatterns = [
    path("<str:hash_data>", home, name='main_1'),
    path("", home, name='main_2'),

    path('employee/<str:hash_data>',get_employee_list , name='employee'),
    path('employee/delete/<int:pk>', delete_employee , name='employee_delete'),
    path('employee/create/<str:hash_data>',create_employee , name='employee_create'), 

    path('trucks/<str:hash_data>', get_trucks_list , name='trucks'),
    path('truck/create/<str:hash_data>',create_truck , name='truck_create'),
    path('truck/confirm/<str:hashed_data>/<uuid:pk>',confirm_truck , name='confirm_truck'),

    path('reports/<str:hash_data>', get_report_list, name="reports"),
    path('server-time/', server_time, name="server_time"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

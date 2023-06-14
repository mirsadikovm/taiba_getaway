from django.urls import path
from worker.views import log_user_in
urlpatterns = [
    path('login/', log_user_in, name='login'), # type: ignore
]

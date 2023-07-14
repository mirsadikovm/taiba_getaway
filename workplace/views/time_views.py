from django.http import JsonResponse
from django.utils import timezone


def server_time(request):
    now = timezone.now()
    response_data = {'server_time': now.strftime('%Y-%m-%d %H:%M:%S')}
    return JsonResponse(response_data)
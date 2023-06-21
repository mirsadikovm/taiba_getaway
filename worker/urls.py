from django.urls import path
from worker.views import log_user_in
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', log_user_in, name='login'), # type: ignore
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


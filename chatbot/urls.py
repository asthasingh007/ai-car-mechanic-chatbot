from django.urls import path
from .views import chat, diagnosis, booking, get_booking, upload_media

urlpatterns = [
    path("chat/", chat),
    path("diagnosis/", diagnosis),
    path("booking/", booking),
    path("booking/<int:id>/", get_booking),
    path("upload/", upload_media),
]
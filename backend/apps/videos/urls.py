from django.urls import path
from .views import VideoAPIView

app_name = 'videos'

urlpatterns = [
    path('latest/', VideoAPIView.as_view()),
]

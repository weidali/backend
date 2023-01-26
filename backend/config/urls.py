from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from posts.views import PostViewSet
from videos.views import VideoViewSet

schema_view = get_swagger_view(title='Demo API')

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'videos', VideoViewSet, basename='videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

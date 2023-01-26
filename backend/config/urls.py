from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from posts.views import PostViewSet

schema_view = get_swagger_view(title='Demo API')

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += router.urls

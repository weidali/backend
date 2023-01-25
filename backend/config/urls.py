from django.contrib import admin
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Demo API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
]

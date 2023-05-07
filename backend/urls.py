from django.contrib import admin
from django.urls import path, include
from optibiz_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

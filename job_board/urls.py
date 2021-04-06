from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.api.urls')),#DRF
    path('', include('jobs.urls')),#固定ページ

]

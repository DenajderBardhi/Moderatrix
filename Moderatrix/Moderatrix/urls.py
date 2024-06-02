# project/urls.py (e.g., Moderatrix/urls.py)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('clients/', include('clients.urls')),
    path('employees/', include('employees.urls')),
   
    path('accounts/', include('accounts.urls')),
]

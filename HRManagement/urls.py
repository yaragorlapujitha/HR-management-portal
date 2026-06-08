from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('attendance/', include('attendance.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('payroll/', include('payroll.urls')),
]
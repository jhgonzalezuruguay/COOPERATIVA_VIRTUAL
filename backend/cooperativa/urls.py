from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('api/beneficios/', include('beneficios.urls')),
    path('api/prestamos/', include('prestamos.urls')),
    path('api/auditoria/', include('auditoria.urls')),
]

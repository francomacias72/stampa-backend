# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Stampa Admin"
admin.site.site_title = "Sustaita-Stampa"
admin.site.index_title = "Bienvenido al Portal de Sustaita Stampa"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
 ]
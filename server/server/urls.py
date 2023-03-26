
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from api.views import getProjects
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", getProjects, basename='getProjects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('api.urls')),
    path('api/', include(route.urls)),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

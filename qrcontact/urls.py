from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from generator import views

urlpatterns = [
    path('' , views.generate_qr , name = 'index'),
    # path('admin/', admin.site.urls),
    # path('', include('generator.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

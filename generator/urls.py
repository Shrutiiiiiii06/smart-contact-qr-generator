# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # Your other URL patterns here
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render

def index(request):
    return render(request, 'generator/index.html')

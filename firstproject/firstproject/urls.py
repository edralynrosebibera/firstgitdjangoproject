from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")  # Loads templates/home.html automatically

urlpatterns = [
    path('', home_view, name='home'),  # Homepage
    path('test/', home_view),          # Optional: still points to same template
    path('admin/', admin.site.urls),
]

# This lets you serve uploaded files (media/) while DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

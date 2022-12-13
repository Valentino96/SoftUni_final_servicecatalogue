from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servicecatalogue.common.urls')),
    path('accounts/', include('servicecatalogue.accounts.urls')),
    path('appointments/', include('servicecatalogue.appointments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

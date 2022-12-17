from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from servicecatalogue.common.views import user_not_unauthorized

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servicecatalogue.common.urls')),
    path('accounts/', include('servicecatalogue.accounts.urls')),
    path('appointments/', include('servicecatalogue.appointments.urls')),
    path('unauthorized', user_not_unauthorized, name='not authorized'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'servicecatalogue.common.views.handler404'
handler500 = 'servicecatalogue.common.views.handler500'

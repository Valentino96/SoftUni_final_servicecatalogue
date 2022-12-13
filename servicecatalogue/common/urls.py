from django.urls import path

from servicecatalogue.common.views import index, add_service, details_service, edit_service, delete_service, \
    like_service, comment_service

urlpatterns = [path('', index, name='index'),
               path('add/service/', add_service, name='add service'),
               path('details/service/<slug:service_slug>/', details_service, name='details service'),
               path('edit/service/<slug:service_slug>/', edit_service, name='edit service'),
               path('delete/service/<slug:service_slug>/', delete_service, name='delete service'),
               path('like/<int:service_id>/', like_service, name='like service'),
               path('comment/<int:service_id>/', comment_service, name='comment service')
               ]


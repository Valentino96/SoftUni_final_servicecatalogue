from django.urls import path

from servicecatalogue.appointments.views import booking, make_booking, appointments_list, customer_appointments

urlpatterns = [
    path('booking/<slug:service_slug>/', booking, name='booking'),
    path('booking-submit/<slug:service_slug>/', make_booking, name='booking_submit'),
    path('booking-list/', appointments_list, name='provider appointments'),
    path('customer-list/', customer_appointments, name='customer appointments')]

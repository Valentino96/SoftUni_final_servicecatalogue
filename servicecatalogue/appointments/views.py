from datetime import datetime, timedelta

from django.views import generic as views
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from servicecatalogue.accounts.models import CustomerProfile, ProviderProfile
from servicecatalogue.appointments.models import Appointment
from servicecatalogue.common.models import Service
from servicecatalogue.core.appointment_utils import valid_weekday, is_weekday_valid, check_time, day_to_weekday

UserModel = get_user_model()


def booking(request, service_slug):
    weekdays = valid_weekday(21)
    valid_weekdays = is_weekday_valid(weekdays)
    service = Service.objects.filter(slug=service_slug).get()
    if request.method == 'POST':
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking')

        request.session['day'] = day
        #request.session['service'] = service

        return redirect('booking_submit', service_slug=service.slug)

    return render(request, 'bookings/booking.html', {
        'weekdays': weekdays,
        'valid_weekdays': valid_weekdays,
        'service': service
    })


def make_booking(request, service_slug):
    customer = CustomerProfile.objects.filter(user_id=request.user.pk).get()
    times = [
         '10', '11', '12', '13', '14', '15', '16', '17', '18'
    ]
    today = datetime.now()
    min_date = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    max_date = strdeltatime
    day = request.session.get('day')
    service = Service.objects.filter(slug=service_slug).get()
    provider = ProviderProfile.objects.filter(user_id=service.provider_id).get()

    hour = check_time(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = day_to_weekday(day)
        if service != None:
            if day <= max_date and day >= min_date:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                    if Appointment.objects.filter(date=day).count() < 11:
                        if Appointment.objects.filter(date=day, timeslot=time).count() < 1:
                            AppointmentForm = Appointment.objects.create(
                                customer=customer,
                                provider=provider,
                                service=service,
                                date=day,
                                timeslot=time,
                            )
                            messages.success(request, "Appointment Saved!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return render(request, 'bookings/submit_booking.html', {
        'times': hour,
        'service': service,
    })


def appointments_list(request):
    user = request.user
    items = Appointment.objects.filter(provider__user_id=user.pk).order_by('date', 'timeslot')

    return render(request, 'bookings/appointments-provider.html', {
        'items': items,
        'user': user,
    })


def customer_appointments(request):
    user = request.user
    items = Appointment.objects.filter(customer__user_id=user.pk).order_by('date', 'timeslot')

    return render(request, 'bookings/appointments-provider.html', {
        'items': items,
        'user': user,
    })

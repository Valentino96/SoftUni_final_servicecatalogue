from datetime import datetime, timedelta

from servicecatalogue.appointments.models import Appointment


def day_to_weekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def valid_weekday(days):
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def is_weekday_valid(x):
    valid_week_days = []
    for j in x:
        if Appointment.objects.filter(date=j).count() < 10:
            valid_week_days.append(j)
    return valid_week_days


def check_time(times, day):
    x = []
    for k in times:
        if Appointment.objects.filter(date=day, timeslot=k).count() < 1:
            x.append(k)
    return x

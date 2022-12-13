from servicecatalogue.common.models import Service


def get_service_by_slug(service_slug):
    return Service.objects \
        .filter(slug=service_slug) \
        .get()


def is_owner(request, obj):
    return request.user == obj.provider


def get_service_slug(request, service_id):
    return request.META['HTTP_REFERER'] + f'#service-{service_id}'

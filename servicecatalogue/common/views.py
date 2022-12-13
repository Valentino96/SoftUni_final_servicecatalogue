from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import slugify
from servicecatalogue.common.forms import AddServiceForm, SearchServiceForm, EditServiceForm, DeleteServiceForm, \
    ServiceCommentForm
from servicecatalogue.common.models import Service, ServiceLike
from servicecatalogue.core.service_utils import is_owner, get_service_slug, \
    get_service_by_slug


def index(request):
    search_form = SearchServiceForm(request.POST)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['type']

    services = Service.objects.filter(type=search_pattern)

    context = {
        'services': services,
        'search_form': search_form,
    }

    return render(
        request,
        'common/index.html',
        context,
    )


@login_required
def add_service(request):
    if request.method == 'GET':
        form = AddServiceForm()
    else:
        form = AddServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.slug = slugify(f'{service.provider.id}-{service.type}')
            service.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'common/add-service.html', context)


def details_service(request, service_slug):
    service = get_service_by_slug(service_slug)
    likes_count = service.servicelike_set.count()
    context = {
        'service': service,
        'likes_count': likes_count,
        'is_owner': service.provider == request.user,
    }

    return render(
        request,
        'common/services-details.html',
        context,
    )


@login_required()
def edit_service(request, service_slug):
    service = get_service_by_slug(service_slug)

    if not is_owner(request, service):
        return redirect('details service', service_slug=service_slug)

    if request.method == 'GET':
        form = EditServiceForm(instance=service)
    else:
        form = EditServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('details service', service_slug=service_slug)

    context = {
        'form': form,
        'service_slug': service_slug,
    }

    return render(
        request,
        'common/service-edit.html',
        context,
    )


@login_required()
def delete_service(request, service_slug):
    service = get_service_by_slug(service_slug)

    if not is_owner(request, service):
        return redirect('details service',  service_slug=service_slug)

    if request.method == 'GET':
        form = DeleteServiceForm(instance=service)
    else:
        form = DeleteServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'service_slug': service_slug,
    }

    return render(
        request,
        'common/service-delete.html',
        context,
    )


@login_required
def like_service(request, service_id):
    user_liked_service = ServiceLike.objects \
        .filter(service_id=service_id, user=request.user.pk)

    if user_liked_service:
        user_liked_service.delete()
    else:
        ServiceLike.objects.create(
            service_id=service_id,
            user_id=request.user.pk,
        )

    return redirect(get_service_slug(request, service_id))


@login_required
def comment_service(request, service_slug):
    service = Service.objects.filter(slug=service_slug) \
        .get()

    form = ServiceCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.service = service
        comment.save()

    return redirect('index')

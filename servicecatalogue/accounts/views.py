from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from servicecatalogue.accounts.forms import CustomerCreateForm, ProviderCreateForm, CustomerEditForm, ProviderEditForm
from servicecatalogue.accounts.models import CustomerProfile, ProviderProfile

UserModel = get_user_model()


class SignUpView(views.TemplateView):
    template_name = 'accounts/sign-up.html'


class CustomerSignUpView(views.CreateView):
    model = UserModel
    form_class = CustomerCreateForm
    template_name = 'accounts/customer sign up.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class ProviderSignUpView(views.CreateView):
    model = UserModel
    form_class = ProviderCreateForm
    template_name = 'accounts/provider sign up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'provider'
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response

    success_url = reverse_lazy('index')


class UserSignInView(auth_views.LoginView):
    template_name = 'accounts/sign in.html'
    success_url = reverse_lazy('common.index')


class UserSignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class CustomerDetailsView(views.DetailView):
    template_name = 'accounts/customer-details.html'
    model = CustomerProfile

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailsView, self).get_context_data(**kwargs)
        context['user'] = CustomerProfile.objects.filter(user=self.get_object())
        return context


class ProviderDetailsView(views.DetailView):
    template_name = 'accounts/provider-details.html'
    model = ProviderProfile

    def get_context_data(self, **kwargs):
        context = super(ProviderDetailsView, self).get_context_data(**kwargs)
        context['user'] = ProviderProfile.objects.filter(user=self.get_object())
        return context


class CustomerEditView(views.UpdateView):
    template_name = 'accounts/customer-edit.html'
    model = CustomerProfile
    form_class = CustomerEditForm

    def get_success_url(self):
        return reverse_lazy('customer details', kwargs={
            'pk': self.request.user.pk,
        })


class ProviderEditView(views.UpdateView):
    template_name = 'accounts/provider-edit.html'
    model = ProviderProfile
    form_class = ProviderEditForm

    def get_success_url(self):
        return reverse_lazy('provider details', kwargs={
            'pk': self.request.user.pk,
        })


class CustomerDeleteView(views.DeleteView):
    template_name = 'accounts/customer-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


class ProviderDeleteView(views.DeleteView):
    template_name = 'accounts/provider-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')





from django.urls import path

from servicecatalogue.accounts.views import CustomerSignUpView, ProviderSignUpView, UserSignInView, \
    UserSignOutView, CustomerDetailsView, ProviderDetailsView, CustomerEditView, ProviderEditView, \
    CustomerDeleteView, ProviderDeleteView, SignUpView

urlpatterns = (
    path('sign-up/customer/', CustomerSignUpView.as_view(), name='customer sign up'),
    path('sign-up/provider/', ProviderSignUpView.as_view(), name='provider sign up'),
    path('sign-in/', UserSignInView.as_view(), name='sing in'),
    path('sign-out/', UserSignOutView.as_view(), name='sing out'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('details/customer/<int:pk>/', CustomerDetailsView.as_view(), name='customer details'),
    path('details/provider/<int:pk>/', ProviderDetailsView.as_view(), name='provider details'),
    path('edit/provider/<int:pk>/', ProviderEditView.as_view(), name='provider edit'),
    path('edit/customer/<int:pk>/', CustomerEditView.as_view(), name='customer edit'),
    path('delete/provider/<int:pk>/', ProviderDeleteView.as_view(), name='provider delete'),
    path('delete/customer/<int:pk>/', CustomerDeleteView.as_view(), name='customer delete'),
)

from django.http import HttpResponseRedirect
from django.urls import path, reverse_lazy

from .views import UserLoginApiView, UserRegistrationApiView

urlpatterns = [
    path('', lambda r: HttpResponseRedirect(reverse_lazy('url_login')), name='url-home'),
    path('login/', UserLoginApiView.as_view(), name='url_login'),
    path('register/', UserRegistrationApiView.as_view(), name='url_registration'),
]

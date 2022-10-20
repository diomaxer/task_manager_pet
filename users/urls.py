from django.urls import path
from users.views import sign_up, log_in, log_out


urlpatterns = [
    path('signup', sign_up, name='sign_up'),
    path('login', log_in, name='log_in'),
    path('logout', log_out, name='log_out'),
]
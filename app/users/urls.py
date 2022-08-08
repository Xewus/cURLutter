from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path(
        'password-reset/',
        views.ChangePasswordView.as_view(),
        name='password_reset'
    )
]

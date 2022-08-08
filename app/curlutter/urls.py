from django.urls import path

from . import views

app_name = 'curlutter'


urlpatterns = [
    path('add-link/', views.add_link, name='add'),
    path('help/', views.help, name='help'),
    path('<short>/', views.link, name='link'),
]

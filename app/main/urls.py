from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('link/', include('curlutter.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]

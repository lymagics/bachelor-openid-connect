from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('api/v1/', include('api.urls')),
    path('users/', include('users.urls')),
    path('oauth2/', include('oauth2_provider.urls',
                            namespace='oauth2_provider')),
]

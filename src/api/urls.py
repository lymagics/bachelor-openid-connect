from django.urls import path

from users.api.views import user_get

urlpatterns = [
    path('users/me/', user_get, name='me'),
]

app_name = 'api'

from django.urls import path
from .views import register_page, register_attempt

app_name = 'empresa'
urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('register/try/', register_attempt),
]

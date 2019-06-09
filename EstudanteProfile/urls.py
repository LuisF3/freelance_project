from django.urls import path
from .views import home_page, register_page, register_attempt, work_detail, subscribe, unsubscribe, subscribed_works


app_name = 'estudante'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('subscribed/', subscribed_works, name='subscribed_works'),
    path('<int:work_pk>/', work_detail, name='work_detail'),
    path('<int:work_pk>/subscribe/', subscribe),
    path('<int:work_pk>/unsubscribe/', unsubscribe),
    path('register/', register_page, name='register_page'),
    path('register/try/', register_attempt),
]

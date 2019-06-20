from django.urls import path
from .views import home_page, register_page, register_attempt, work_detail, subscribe, unsubscribe, subscribed_works,\
    account_information, account_information_update, search_works


app_name = 'estudante'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('subscribed/', subscribed_works, name='subscribed_works'),
    path('register/', register_page, name='register_page'),
    path('register/try/', register_attempt),
    path('account/', account_information, name='account_information'),
    path('account/update/', account_information_update, name='account_information_update'),
    path('search/', search_works, name='search_work'),
    path('<int:work_pk>/', work_detail, name='work_detail'),
    path('<int:work_pk>/subscribe/', subscribe),
    path('<int:work_pk>/unsubscribe/', unsubscribe),
]

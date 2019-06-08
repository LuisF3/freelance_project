from django.urls import path
from .views import all_works, add_work, add_work_attempt, subscribe_student, \
                   subscribe_student_attempt, unsubscribe_student_attempt,\
                   students_subscribed, students_subscribed_detail


app_name = 'trabalho'
urlpatterns = [
    path('', all_works, name='all_works'),
    path('add/', add_work, name='add_work'),
    path('add/try/', add_work_attempt),
    path('subscribe/<int:pk>/', subscribe_student, name='subscribe_student'),
    path('subscribe/<int:pk>/try/', subscribe_student_attempt),
    path('unsubscribe/<int:pk>/try/', unsubscribe_student_attempt, name='unsubscribe_attempt'),
    path('subscribers/<int:work_pk>/', students_subscribed, name='students_subscribed'),
    path('subscribers/<int:work_pk>/<int:student_pk>/', students_subscribed_detail, name='students_subscribed_detail'),
]

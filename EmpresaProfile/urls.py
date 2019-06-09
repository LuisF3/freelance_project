from django.urls import path, include
from .views import home_page, register_page, register_attempt, work_detail, hire_student, refuse_student, add_work

app_name = 'empresa'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('add-work/', add_work, name='add_work'),
    path('<int:work_pk>/', work_detail, name='work_detail'),
    path('<int:work_pk>/hire/<int:student_pk>/', hire_student),
    path('<int:work_pk>/refuse/<int:student_pk>/', refuse_student),
    path('register/', register_page, name='register_page'),
    path('register/try/', register_attempt),
]

from django.urls import path, include
from .views import home_page, register_page, register_attempt, work_detail, hire_student, refuse_student, add_work, \
    fire_student, work_delete, private_control, account_information, account_information_update


# urls de responsabilidade do app EmpresaProfile. app_name é uma referência
# para encontrar as urls mais facilmente

app_name = 'empresa'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('add-work/', add_work, name='add_work'),
    path('register/', register_page, name='register_page'),
    path('register/try/', register_attempt),
    path('account/', account_information, name='account_information'),
    path('account/update/', account_information_update, name='account_information_update'),
    path('<int:work_pk>/', work_detail, name='work_detail'),
    path('<int:work_pk>/delete/', work_delete, name='work_delete'),
    path('<int:work_pk>/control_private/', private_control, name='private_control'),
    path('<int:work_pk>/hire-<int:student_pk>/', hire_student),
    path('<int:work_pk>/refuse-<int:student_pk>/', refuse_student),
    path('<int:work_pk>/fire-<int:student_pk>/', fire_student),
]

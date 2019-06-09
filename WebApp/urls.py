from django.urls import path, include
from .views import home, login_page, login_attempt, register_page, logout_page, profile_page


app_name = 'webapp'
urlpatterns = [
    path('', home, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('login/try/', login_attempt),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
    path('student/', include('EstudanteProfile.urls', namespace='estudante')),
    path('business/', include('EmpresaProfile.urls', namespace='empresa')),
    path('<username>/', profile_page, name='profile_page'),
]

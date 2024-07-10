# urls.py
from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password-reset-confirm/<int:user_id>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("add-patient/", views.quick_add_patient, name="quick_add_patient"),
    path('patients/', views.all_patients, name='all-patients'),
    path('patients/add', views.add_patient, name='add-patient'),
    path('patients/update/<int:id>', views.update_patient, name="update-patient"),
    path('patients/delete/<int:id>', views.delete_patient, name="delete-patient"),

]

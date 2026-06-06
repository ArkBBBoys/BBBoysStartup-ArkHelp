from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit-profile/', views.edit_profile, name='edit_profile'),
    path('dashboard/edit-helper-profile/', views.edit_helper_profile, name='edit_helper_profile'),
]

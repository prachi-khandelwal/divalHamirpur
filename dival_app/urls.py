from django.urls import path
from . import views
app_name = 'dival_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('formlogin/',views.login_user,name='login_user'),
]

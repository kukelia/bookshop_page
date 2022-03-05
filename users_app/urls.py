from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name = 'user_index'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('sign_up', views.sign_up, name = 'sign_up')
]
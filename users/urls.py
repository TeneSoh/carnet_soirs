from django.urls import path
from . import views
urlpatterns = [
    path('', views.signIn , name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.disconnect, name='logout'),
]

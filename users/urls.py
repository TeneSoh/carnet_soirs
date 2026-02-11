from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name="sign_in"),
    path('logout/', views.disconnect, name="logout"),
    path('register/', views.register, name="register"),
]

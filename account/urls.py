from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', auth_view.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.disconnect, name='logout'),
]

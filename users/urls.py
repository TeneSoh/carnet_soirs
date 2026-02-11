from django.urls import path
from . import views
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', views.signIn, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.disconnect, name='logout'),
]

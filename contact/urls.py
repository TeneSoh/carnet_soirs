from django.urls import path

# from .views import index , store , delete , show , edit#, create
from . import views
urlpatterns = [
    # path('', index, name="contact"),
    path('', views.ListContact.as_view(), name="contact"),
    # path('create/', create, name="create_contact"),
    # path('store/', views.store, name="store_contact"),
    path('store/', views.CreateContactView.as_view(), name="store_contact"),
    # path('delete-contact/<int:id>', views.delete, name="delete_contact"),
    path('delete-contact/<int:pk>', views.DeleteContactView.as_view(), name="delete_contact"),
    path('show-contact/<int:id>', views.show, name="show_contact"),
    path('edit-contact/<int:id>', views.edit, name="edit_contact"),
    # path('update-contact/<int:id>', update, name="update_contact"),
    
]
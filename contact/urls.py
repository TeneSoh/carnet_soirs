from django.urls import path

# from .views import index , store , delete , show , edit#, create
from . import views
urlpatterns = [
    path('', views.ListContact.as_view, name="contact"),
    path('', views.ContactCreateView.as_view, name="contact_create"),
    # path('create/', create, name="create_contact"),
    path('store/', views.store, name="store_contact"),
    path('delete-contact/<int:id>', views.delete, name="delete_contact"),
    path('show-contact/<int:id>', views.show, name="show_contact"),
    path('edit-contact/<int:id>', views.edit, name="edit_contact"),
    # path('update-contact/<int:id>', update, name="update_contact"),
    
]
from django.urls import path

from contact.views import DetailContactView
# from .views import index , store , delete , show , edit#, create
from . import views
urlpatterns = [
    path('', views.index, name="contact"),
    #path('', views.ListContact.as_view(), name="contact"),
    # path('create/', create, name="create_contact"),
    # path('store/', views.store, name="store_contact"),
    path('store/', views.CreateContactView.as_view(), name="store_contact"),
    # path('delete-contact/<int:id>', views.delete, name="delete_contact"),
    path('delete-contact/<int:pk>', views.DeleteContactView.as_view(), name="delete_contact"),
    # path('show-contact/<int:id>', views.show, name="show_contact"),
    path('show-contact/<int:pk>', views.DetailContactView.as_view(), name="show_contact"),
    path('edit-contact/<int:pk>', views.UpdateContactView.as_view(), name="edit_contact"),
    # path('update-contact/<int:id>', update, name="update_contact"),
    
]
from django.db.models.signals import post_delete, post_migrate, post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.contrib import contenttypes
from contact.models import Contact

User = get_user_model()


@receiver(post_migrate)
def create_roles_and_permissions(sender, **kwargs):
    admin_groupe, create = Group.objects.get_or_create(name='admin')
    if create:
        print('le role a ete creer')
    else:
        print('le role existe deja')


    user_groupe, _ = Group.objects.get_or_create(name='user')

    content_type = ContentType.objects.get_for_model(Contact)

    can_view_all_contacts,_ = Permission.objects.get_or_create(codename='can_view_all_contacts', name='Peut voir tout les contacts',content_type = content_type)

    can_hide_contact,_ = Permission.objects.get_or_create(codename='can_hide_contacts',name ='Peut cacher un contacts', content_type = content_type)

    add_contact,_ = Permission.objects.get_or_create(codename='add_contact',name ='Can add contact', content_type = content_type)

    change_contact,_ = Permission.objects.get_or_create(codename='change_contact',name ='Can change contact', content_type = content_type)

    admin_groupe.permissions.add(can_view_all_contacts) #type:ignore
    user_groupe.permissions.add(can_hide_contact) #type:ignore
    user_groupe.permissions.add(add_contact) #type:ignore
    user_groupe.permissions.add(change_contact) #type:ignore
 
@receiver(post_save, sender=User)
def assign_user_to_groupe(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='user')
        instance.groups.add(group)
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(user_signed_up)
def assign_customer_group(request, user, **kwargs):
    """
    When a new user signs up through Allauth,
    automatically add them to the 'Customer' group.
    """
    group, _ = Group.objects.get_or_create(name="Customer")
    user.groups.add(group)
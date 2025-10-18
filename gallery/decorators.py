from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

def superuser_required(view_func):
    """
    Decorator for views that allows access only to superusers.
    """
    return user_passes_test(lambda u: u.is_superuser)(view_func)

def superuser_required_cbv(cls):
    """Apply superuser_required to class-based views."""
    cls.dispatch = method_decorator(superuser_required)(cls.dispatch)
    return cls

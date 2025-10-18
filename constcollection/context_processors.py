from allauth.account.forms import LoginForm, SignupForm
from django.utils import timezone

def auth_forms(request):
    """
    Makes login and signup forms available to every template.
    """
    return {
        'login_form': LoginForm(),
        'signup_form': SignupForm(),
    }

def upcoming_exhibitions(request):
    """
    Makes upcoming exhibitions available to every template.
    """
    from exhibitions.models import Exhibition
    today = timezone.now().date()
    upcoming = Exhibition.objects.filter(start_date__gt=today).order_by('start_date')[:3]
    return {
        'upcoming_exhibitions': upcoming,
    }
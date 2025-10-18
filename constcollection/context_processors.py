from allauth.account.forms import LoginForm, SignupForm

def auth_forms(request):
    """
    Makes login and signup forms available to every template.
    """
    return {
        'login_form': LoginForm(),
        'signup_form': SignupForm(),
    }
from types import SimpleNamespace
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .forms import ContactForm


def contact_view(request):
    """Render contact form, save messages and send notification email."""
    # small context object for template
    # use SimpleNamespace for attribute access
    contact = SimpleNamespace(
        title="Const Collection",
        content="",
        updated_on=timezone.now(),
        email=getattr(settings, 'DEFAULT_FROM_EMAIL', ''),
        phone=''
    )

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            # attempt to send notification to site owner
            subject = f"Contact form: {msg.subject or 'No subject'}"
            body = f"From: {msg.name} <{msg.email}>\n\n{msg.message}"
            recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', None)
            if recipient:
                try:
                    send_mail(
                        subject,
                        body,
                        msg.email,
                        [recipient],
                        fail_silently=True,
                    )
                except Exception:
                    # don't crash on email issues
                    pass
            messages.success(request, "Your message has been sent.")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    context = {
        'collaborate_form': form,
        'contact': contact,
    }
    return render(request, 'contact.html', context)

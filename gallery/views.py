from django.shortcuts import render, get_object_or_404, redirect
from .models import Artwork, Tag
from django.views.generic import TemplateView
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePage(TemplateView):
    """Displays home page"""
    template_name = 'index.html'


class AboutPage(TemplateView):
    """Displays the About page with artist bio, philosophy and process"""
    template_name = 'about.html'


def gallery(request):
    artworks = Artwork.objects.all()
    tags = Tag.objects.all()
    
    # Gets tags 
    tag_slug = request.GET.get('tag')
    if tag_slug:
        artworks = artworks.filter(tags__slug=tag_slug)

    sort = request.GET.get('sort')
    if sort == 'recent':
        artworks = artworks.order_by('-created_at')
    elif sort == 'price_low':
        artworks = artworks.order_by('price')
    elif sort == 'price_high':
        artworks = artworks.order_by('-price')

    context = {
        'artworks': artworks,
        'tags': tags,
        'selected_tag': tag_slug,
        'selected_sort': sort,
    }
    return render(request, 'gallery/gallery.html', context)


def artwork_detail(request, slug):
    artwork = get_object_or_404(Artwork, slug=slug)
    context = {
        'artwork': artwork,
    }
    return render(request, 'gallery/artwork_detail.html', context)


def create_checkout_session(request, art_id):
    artwork = get_object_or_404(
        Artwork,
        pk=art_id,
        is_available=True
    )
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': artwork.title,
                    'images': [artwork.image_url.url],
                },
                'unit_amount': int(artwork.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            '/success?session_id={CHECKOUT_SESSION_ID}'
        ),
        cancel_url=request.build_absolute_uri('/cancel'),
    )
    return redirect(session.url)

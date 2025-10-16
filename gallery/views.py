from django.shortcuts import render, get_object_or_404
from .models import Artwork, Tag, Artist
from django.views.generic import TemplateView


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

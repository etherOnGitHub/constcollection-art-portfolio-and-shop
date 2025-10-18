from django.shortcuts import render
from .models import Exhibition
from gallery.decorators import superuser_required_cbv, superuser_required

# Create your views here.

def exhibition_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'exhibitions/exhibition_list.html', {'exhibitions': exhibitions})

    # Logic to retrieve and display a list of exhibitions
    return render(request, 'exhibitions/exhibition_list.html')

def exhibition_detail(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    return render(request, 'exhibitions/exhibition_detail.html', {'exhibition': exhibition})
    return render(request, 'exhibitions/exhibition_detail.html', {'pk': pk})

@superuser_required
def edit_exhibition(request, pk):
    # Logic to edit an existing exhibition
    return render(request, 'exhibitions/edit_exhibition.html', {'pk': pk})

@superuser_required
def create_exhibition(request):
    # Logic to create a new exhibition
    return render(request, 'exhibitions/create_exhibition.html')


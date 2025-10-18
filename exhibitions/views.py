from django.shortcuts import render

from exhibitions.forms import ExhibitionForm
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

@superuser_required
def edit_exhibition(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    form = ExhibitionForm(request.POST or None, request.FILES or None, instance=exhibition)
    if form.is_valid():
        form.save()
        return render(request, 'exhibitions/exhibition_detail.html', {'exhibition': exhibition})
    return render(request, 'exhibitions/edit_exhibition.html', {'form': form, 'exhibition': exhibition})

@superuser_required
def create_exhibition(request):
    form = ExhibitionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return render(request, 'exhibitions/exhibition_list.html')

    return render(request, 'exhibitions/create_exhibition.html')

@superuser_required
def delete_exhibition(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    exhibition.delete()
    return render(request, 'exhibitions/exhibition_list.html')

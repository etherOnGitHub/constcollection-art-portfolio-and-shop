from django.shortcuts import render, get_object_or_404, redirect
from exhibitions.forms import ExhibitionForm
from .models import Exhibition
from gallery.decorators import superuser_required

def exhibition_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'exhibitions/exhibition_list.html', {'exhibitions': exhibitions})

# View exhibition details
def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    return render(request, 'exhibitions/exhibition_detail.html', {'exhibition': exhibition})

@superuser_required
def create_exhibition(request):
    form = ExhibitionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        exhibition = form.save()
        return redirect('exhibitions:exhibition_detail', pk=exhibition.pk)
    return render(request, 'exhibitions/create_exhibition.html', {'form': form})

@superuser_required
def edit_exhibition(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    form = ExhibitionForm(request.POST or None, request.FILES or None, instance=exhibition)
    if form.is_valid():
        form.save()
        return redirect('exhibitions:exhibition_detail', pk=exhibition.pk)
    return render(request, 'exhibitions/edit_exhibition.html', {'form': form, 'exhibition': exhibition})

@superuser_required
def delete_exhibition(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    exhibition.delete()
    return redirect('exhibitions:exhibition_list')

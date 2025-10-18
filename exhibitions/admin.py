from django.contrib import admin

from exhibitions.models import Exhibition

# Register your models here.

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'video', 'start_date', 'end_date')
    search_fields = ('title',)

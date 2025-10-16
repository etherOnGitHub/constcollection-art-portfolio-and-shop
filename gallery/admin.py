from django.contrib import admin
from .models import Artist, Artwork
# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
    search_fields = ('name',)


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'is_available', 'created_at')
    list_filter = ('is_available', 'artist', 'created_at')
    search_fields = ('title', 'artist__name')
    prepopulated_fields = {'slug': ('title',)}

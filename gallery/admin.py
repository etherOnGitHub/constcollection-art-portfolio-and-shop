from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Artist, Artwork, Tag
# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(SummernoteModelAdmin):
    list_display = ('title', 'artist', 'price', 'is_available', 'created_at')
    list_filter = ('is_available', 'artist', 'created_at')
    search_fields = ('title', 'artist__name')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
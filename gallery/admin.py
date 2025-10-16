from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from cloudinary.utils import cloudinary_url
from .models import Artist, Artwork, Tag
# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(SummernoteModelAdmin):
    list_display = ('thumbnail_list', 'title', 'artist', 'price', 'is_available', 'created_at')
    list_filter = ('is_available', 'artist', 'created_at', 'tags')
    search_fields = ('title', 'artist__name')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    
    readonly_fields = ('thumbnail_preview',)

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'artist',
                'price',
                'is_available',
                'image_url',
                'thumbnail_preview', 
                'description',
                'tags',
            ),
        }),
    )

    def thumbnail_list(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />',
                obj.image_url.url
            )
        return "No Image"
    thumbnail_list.short_description = "Thumbnail"

    def thumbnail_preview(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" width="300" style="object-fit: cover; border-radius: 10px;" />',
                obj.image_url.url
            )
        return "No Image"
    thumbnail_preview.short_description = "Current Thumbnail"
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
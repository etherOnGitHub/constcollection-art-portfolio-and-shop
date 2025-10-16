from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import Artist, Artwork, Tag
# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(SummernoteModelAdmin):
    list_display = ('title', 'artist', 'price', 'is_available', 'created_at')
    list_filter = ('is_available', 'artist', 'created_at')
    search_fields = ('title', 'artist__name')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

    def thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image_url.url)
        return "-"
    
    thumbnail.short_description = 'Thumbnail'
    thumbnail.admin_order_field = 'image_url'
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
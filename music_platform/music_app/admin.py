from django.contrib import admin
from .models import Song, Playlist

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'duration')
    search_fields = ('title', 'artist')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

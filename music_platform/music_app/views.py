from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, SongForm, PlaylistForm
from django.shortcuts import render
from .models import Song
from django.shortcuts import render
from .models import Song, Playlist

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music_app/song_list.html', {'songs': songs})

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'music_app/playlist_list.html', {'playlists': playlists})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music_app/song_list.html', {'songs': songs})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})

def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return redirect('home')
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form': form})

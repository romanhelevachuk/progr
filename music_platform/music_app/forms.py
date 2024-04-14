from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Song, Playlist

# Форма для реєстрації користувача
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Форма для входу користувача
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Форма для моделі Song
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'duration']

# Форма для моделі Playlist
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'description']

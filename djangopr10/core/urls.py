from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('auth/', include('authentication.urls')),
    path('', include('polls.urls')),
]

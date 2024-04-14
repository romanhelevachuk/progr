from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music_app.urls')), # Переконайтеся, що цей рядок присутній
]

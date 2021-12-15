from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', main_page),
    path('feed', feed),
    path('profile/<int:profile_id>', ProfileView.as_view(), name='profile'),
    path('profile/subscribe/<int:profile_id>', subscribe)
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
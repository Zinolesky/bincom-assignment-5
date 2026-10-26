from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_gallery, name='media_gallery'),
    path('media/<int:pk>/', views.media_detail, name='media_detail'),
    path('upload/', views.upload_media, name='upload_media'),
]

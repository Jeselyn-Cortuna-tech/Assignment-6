from django.urls import path
from .views import (
    GalleryListView,
    PhotoUpdateView,
    PhotoDeleteView
)

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery_home'),

    path(
        'photo/<int:pk>/edit/',
        PhotoUpdateView.as_view(),
        name='edit_photo'
    ),

    path(
        'photo/<int:pk>/delete/',
        PhotoDeleteView.as_view(),
        name='delete_photo'
    ),
]
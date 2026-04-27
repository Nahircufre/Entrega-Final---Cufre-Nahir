from django.urls import path
from . import views
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
    InboxView,
    SentView,
    MensajeCreateView,
    MensajeDetailView
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🏠 HOME
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # 📄 PAGES
    path('pages/', PageListView.as_view(), name='pages'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),

    # 💬 MENSAJERÍA
    path('messages/inbox/', InboxView.as_view(), name='inbox'),
    path('messages/sent/', SentView.as_view(), name='sent'),
    path('messages/new/', MensajeCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/', MensajeDetailView.as_view(), name='message_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

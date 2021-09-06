from django.urls import path
from .views import HomeView, AboutDetailView, MyListView, ContactDetailView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutDetailView, name='about-detail'),
    path('contact/', ContactDetailView, name='contact-detail'),
    path('posts/', MyListView.as_view(), name='list-detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

from django.urls import path, re_path
from .views import home, about, book, menu, display_menu_item
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('menu/', menu, name="menu"),
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item")
]
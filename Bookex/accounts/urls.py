# account/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationView
from .views import home,my_books,request_history
from . import views


urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', views.login_page, name='user_login'),
    path('logout/', views.log_out, name='logout'),
    path('hi/', views.say_hi),
    path('home/', home.as_view(), name='home'),
    path('book/<book_id>/', views.book_details, name='book_details'),
    path('profile/', views.profile, name='profile'),
    path('add_book/', views.add_book, name='add_book'),
    path('my_books/', my_books.as_view(), name='my_books'),
    path('exchange/<book_id>/', views.exchange, name='exchange'),
    path('request_history/', request_history.as_view(), name='request_history'),
    path('accept/<ex_id>/', views.accept, name='accept'),
    path('phone/<username>/', views.phone, name='phone'),

    # Add other URL patterns as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
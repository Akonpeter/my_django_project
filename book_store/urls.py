from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('user/', views.user_home, name='user_home'),
]

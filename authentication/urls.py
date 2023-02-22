from django.urls import path
from .views import UserCreate, Login

auth_patterns = [
    path('signup/', UserCreate.as_view(), name = 'user_create'),
    path('login/', Login.as_view(), name = 'login'),
]
from django.urls import path
from .views import UserListCreate, UserRetrieve

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<str:user_id>/', UserRetrieve.as_view(), name='user-retrieve'),
]

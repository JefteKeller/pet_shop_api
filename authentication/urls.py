from django.urls import path
from .views import UserView, ProtectedView, LoginView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', LoginView.as_view()),
    path('users/protected/', ProtectedView.as_view())
]

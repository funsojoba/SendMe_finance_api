from django.urls import path

from .views.register import RegisterView
from .views.login import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]

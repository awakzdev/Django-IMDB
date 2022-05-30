from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.signup_view, name='login'),
]

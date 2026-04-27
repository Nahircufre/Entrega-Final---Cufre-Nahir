from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    # 🚪 LOGOUT
    path('logout/', LogoutView.as_view(), name='logout'),
]
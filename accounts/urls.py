from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),

    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),

    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path(
        'password/',
        PasswordChangeView.as_view(
            template_name='accounts/change_password.html',
            success_url='/accounts/password_done/'
        ),
        name='change_password'
    ),

    path(
        'password_done/',
        PasswordChangeDoneView.as_view(
            template_name='accounts/password_done.html'
        ),
        name='password_done'
    ),
]
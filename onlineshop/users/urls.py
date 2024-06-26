from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account/login', views.login, name='login'),
    path('account/register', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    
    # path('users-cart/', views.users_cart, name='users_cart'),
    
]
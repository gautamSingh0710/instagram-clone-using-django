from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='home'),
    path('signup/', views.signup, name='register'),
    path('login_view/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('message/',views.message,name='message'),
    path('search/',views.search,name='search'),
    path('profile/',views.profile,name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('music/',views.music,name='music'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('reels/',views.reels,name='reels'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    
]

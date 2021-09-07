from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('like',like,name='like'),
    path('add-comment/<int:pk>',add_comment,name='add-comment'),
    path('signup',signup,name='signup'),
    path('signin',login_user,name='signin'),
    path('logout',logout_user,name='logout'),
    path('post_create',post_create,name='post_create'),
    path('profile/<int:pk>',user_profile,name='profile'),
    path('noti',notification,name='noti')
]
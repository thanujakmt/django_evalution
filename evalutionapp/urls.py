
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('user_face/', views.user_face_view ,name='userface'),
    path('app/',views.app_view,name='app'),
    path('login/',views.login_view,name='login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('register/',views.register_view,name='register'),
]
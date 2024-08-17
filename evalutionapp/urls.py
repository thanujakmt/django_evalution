
from django.urls import path
from . import views

urlpatterns = [
    path('',views.testview,name='homepage'),
    path('user_face', views.user_face_view ,name='userface')

]
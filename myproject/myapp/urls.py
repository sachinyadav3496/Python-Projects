from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('hello/',views.hello,name='hello'),
    path('hello/<str:id>/',views.hello,name='hello'),
    path('signup/',views.Signup,name='signup'),
    path('mklogin/',views.mklogin,name='mklogin'),
    path('mksignup/',views.mksignup,name='mksignup'),
    path('logout/',views.logout,name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('change_password/',views.change_password),
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('hello/',views.hello,name='hello'),
    path('hello/<str:id>/',views.hello,name='hello'),
    path('signup/',views.Signup,name='signup'),
]

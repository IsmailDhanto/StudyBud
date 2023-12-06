from django.urls import path

from base import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.LogoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('',views.home,name='home'),
    path("rooms/<str:pk>/",views.room,name='rooms'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    
]
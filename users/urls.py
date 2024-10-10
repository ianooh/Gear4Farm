from django.urls import path
from . import views

urlpatterns = [
    path('', views.MachineryListView.as_view(), name='machinery_list'),
    path('machinery/<int:pk>/', views.MachineryDetailView.as_view(), name='machinery_detail'),
    path('machinery/<int:pk>/book/', views.create_booking, name='create_booking'),
    path('profile/', views.profile, name='user_profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('create_booking/', views.create_booking, name='create_booking'),
]

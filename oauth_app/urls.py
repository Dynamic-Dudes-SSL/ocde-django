from django.urls import path
from .views import ProfileView, UserView, AboutUsView

urlpatterns = [
    path('myprofile/<int:id>/',ProfileView.as_view(),name = 'profile'),
    path('users/', UserView.as_view(), name = 'user-list'),
    path('about_us/', AboutUsView.as_view(), name = 'about_us'),
]
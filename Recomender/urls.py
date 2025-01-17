from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name='index'), 
    # path('home/',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('recommend_crop/', views.recommend_crop, name='recommend_crop'),
    path('about_us/', views.about, name='about_us'),   
    path('history/', views.history, name='history'),
    path('logout/', views.user_logout, name='logout'),
]

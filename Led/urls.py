from django.urls import path
from .views import index
from Led import views

app_name = "loginpage"
urlpatterns = [
    path('homepage', views.homepage.as_view(), name="homepage"),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('home', views.home, name='home'),
    path('api/data', views.getAllDataAPIVIEW.as_view(), name="api-data"),
    path('export', views.ExPortCSV, name='export'),
    path('dgt', views.dengiaothong, name='dgt'),
    path('', views.dengiaothong, name='dgtt'),
]
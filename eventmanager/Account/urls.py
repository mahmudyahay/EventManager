from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('newpassword', views.newpassword, name='newpassword'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('userdashboard', views.userdashboard, name='userdashboard'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('adminsearch', views.adminsearch, name='adminsearch'),
    path('task', views.task, name='task'),
    path('admineditstatus', views.admineditstatus, name='admineditstatus')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
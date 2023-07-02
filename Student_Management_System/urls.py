
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views ,Hod_views, Student_views, Staff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    # LOGIN PATH
    path('', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # This is HOD panel url
    path('Hod/Home', Hod_views.HOME, name='hod_home'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from awwards import views as user_views
from django.views.generic.base import TemplateView 
import urllib.request

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('awwards.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/', user_views.register, name='register'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]

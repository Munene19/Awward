from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectDetailView, ProjectListView, ProjectCreateView, ProjectUpdateView
from . import views 

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='home'), 
    url(r'^', views.register, name='register'),
    url(r'^project/<int:pk>/', views.ProjectDetailView, name='project-detail'),
    url(r'^project/new/', views.ProjectCreateView, name='project-create'),
    url(r'^project/<int:pk>/update/', views.ProjectUpdateView, name='project-update'),
    url(r'^api/profiles/', views.ProfileList),
    url(r'^api/projects/', views.ProjectList),
    url(r'^vote/<project/<int:pk/',views.vote, name='vote'),
    url(r'^search/',views.search_project, name='search_project'),
    url(r'^profile/',views.profile,name="profile")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
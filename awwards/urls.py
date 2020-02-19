from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectDetailView, ProjectListView, ProjectCreateView, ProjectUpdateView
from . import views 

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url('', views.home, name='home'),
    url(r'^project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    url(r'^project/new/', ProjectCreateView.as_view(), name='project-create'),
    url(r'^project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    url(r'^api/profiles/', views.ProfileList.as_view()),
    url(r'^api/projects/', views.ProjectList.as_view()),
    url(r'^vote/<project/<int:pk/',views.vote, name='vote'),
    url(r'^search/',views.search_project, name='search_project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
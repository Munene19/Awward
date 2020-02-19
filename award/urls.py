from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^admin/', admin.site.urls),
]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
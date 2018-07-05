from django.conf.urls import url
from geocoding import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.upload_files, name='upload'),
    url(r'^download/(?P<pk>\d+)/$', views.download_files, name='download'),
]

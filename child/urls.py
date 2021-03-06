from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$' ,views.welcome, name='welcome'),
    url(r'^new/',views.create_profile,name='new_profile'),
    url(r'^searched/', views.search_results, name='search_results'),
	url(r'^organization/$', views.organizationIndex, name='organizationIndex'),
	url(r'^organization/$', views.organizationDetails, name='organizationDetails'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

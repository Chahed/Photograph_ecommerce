from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bruno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='home'),
    url(r'^photographs/$', views.photographs, name='photographs'),
    url(r'^films/$', views.films, name='films'),
    url(r'^films/(?P<id>\d+)/$', views.consulterfilm),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^news/$', views.news, name='news'),
    url(r'^shop/$', views.shops, name='shop'),
    url(r'^shop/delivery/$', views.delivery, name='delivery'),
    url(r'^shop/(?P<id>\d+)/$', views.consultershop, name='shopdet'),
    url(r'^photographs/projects/$', views.projects, name='projects'),
    url(r'^photographs/projects/(?P<id>\d+)/(?P<id1>\d+)/$', views.consulter),
     url(r'^photographs/works/$', views.works, name='works'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

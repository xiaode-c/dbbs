from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import urls as main_urls
# from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(main_urls)),
    # url(r'^$', views.index),
]

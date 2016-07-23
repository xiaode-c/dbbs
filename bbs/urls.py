from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import urls as main_urls
from django.conf import settings 
from django.conf.urls.static import static 
# from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(main_urls)),
    # url(r'^$', views.index),
]


if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

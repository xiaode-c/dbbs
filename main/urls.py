from django.conf.urls import patterns, include, url
from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include(main.urls)),
    url(r'^$', views.index),
    url(r'^category/(\d+)/$', views.category, name="category"),
    url(r'^article/(\d+)/$', views.article_detail, name="article_detail"),
    url(r'^account/logout/$', views.account_logout, name="logout"),
    url(r'^account/login/$', views.account_login, name="login"),
    url(r'^article/new/$', views.new_article, name="new_article"),
    url(r'^article/(\d+)/new_comment/$', views.new_comment, name="new_comment"),
    url(r'^account/register/$', views.account_register, name="register"),
    url(r'^(\w+)/user_setting/$', views.user_setting, name="user_setting")
    url(r'^(\w+)/change_avatar/$', views.change_avatar, name="change_avatar")
    
]

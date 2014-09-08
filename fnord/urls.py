from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'home.views.index', name='home'),
    url(r'^$', 'home.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^/', fnord.views.home)
    url(r'^forum/', include('django_simple_forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    #url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change'),
    #url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    #url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset'),
    #url(r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
    #url(r'^accounts/logout/', 'django.contrib.auth.views.logout'),
    # Accounts urls,
)

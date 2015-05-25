from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AndoverRFC3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = patterns('',
                       (r'^(?i)$', 'home.views.index'),
                       (r'^(?i)Home/$', 'home.views.index'),
                       (r'^(?i)Test/$', 'home.views.test'),
                       (r'^(?i)Squads/$', 'squad.views.index'),
                       (r'^(?i)Squads/(?P<squad_id>\d+)/$', 'squad.views.details'),
                       (r'^(?i)News/$', 'news.views.index'),
                       (r'^(?i)News/(?P<news_article_id>\d+)/$', 'news.views.details'),
                       (r'^(?i)Sponsors/$', 'sponsor.views.index'),
                       url(r'^(?i)admin/', include(admin.site.urls)),
                       )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
from django.conf.urls import patterns, include, url
from views import init
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FungiDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'init', init),
)


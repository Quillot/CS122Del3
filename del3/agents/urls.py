from django.conf.urls import url

from . import views as agents_views


urlpatterns = [
    url(r'^$', agents_views.index, name='index'),
    url(r'^generate/$', agents_views.generate, name='generate'),
    url(r'^delete/(?P<agent_id>[0-9]+)/$', agents_views.delete_agent, name='delete_agent')
]
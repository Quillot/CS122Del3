from django.conf.urls import url

from . import views as agents_views


urlpatterns = [
    url(r'^$', agents_views.index, name='index'),
    url(r'^generate/$', agents_views.generate, name='generate'),
    url(r'^delete/(?P<agent_id>[0-9]+)/$', agents_views.delete_agent, name='delete_agent'),
    url(r'^approve/$', agents_views.approve, name='approve'),
    url(r'^approve/(?P<order_id>[0-9]+)/$', agents_views.approve_order, name='approve_order'),
]
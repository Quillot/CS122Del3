from django.conf.urls import url

from . import views as order_views

urlpatterns = [
    url(r'^$', order_views.index, name='index'),
    url(r'^approve/(?P<order_id>[0-9]+)/$', order_views.approve_order, name='approve_order'),
]
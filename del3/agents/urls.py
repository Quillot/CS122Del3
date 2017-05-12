from django.conf.urls import url

from . import views as agents_views


urlpatterns = [
    url(r'^$', agents_views.index, name='index'),
    url(r'^generate/$', agents_views.generate, name='generate'),
]
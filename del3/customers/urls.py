from django.conf.urls import url

from . import views as customer_views

urlpatterns = [
    url(r'^$', customer_views.index, name='index'),
]
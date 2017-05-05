from django.conf.urls import url
from . import views as catalog_views

urlpatterns = [
    url(r'^$', catalog_views.index, name='index'),
    url(r'^addtocart/(?P<product_id>[0-9]+)/$', catalog_views.add_to_cart, name='add_to_cart'),
    url(r'^add/$', catalog_views.add_product, name='add_product'),
    url(r'^delete/(?P<product_id>[0-9]+)/$', catalog_views.delete_product, name='delete_product'),
]
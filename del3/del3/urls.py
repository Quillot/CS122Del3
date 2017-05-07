from django.conf.urls import include, url
from django.contrib import admin
from . import views as del3_views

#index with links to all pages
#admin
#catalog
#signup
#login
#agents
#customers
#orders


urlpatterns = [
	url(r'^$', del3_views.index, name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^catalog/', include('catalog.urls', namespace='catalog')),
	url(r'^agents/', include('agents.urls', namespace='agents')),
	url(r'^customers/', include('customers.urls', namespace='customers')),
	url(r'^orders/', include('orders.urls', namespace='orders')),
	url(r'^cart/', del3_views.cart, name='cart'),
	url(r'^checkout/', del3_views.checkout, name='checkout'),
	url(r'^signup/', del3_views.signup, name='signup'),
	url(r'^signupagent/', del3_views.signup_agent, name='signup_agent'),
	url(r'^setpasswords/', del3_views.set_passwords, name='set_passwords'),
	url(r'^login/', del3_views.login, name='login'),
	url(r'^logout/', del3_views.logout, name='logout'),
]
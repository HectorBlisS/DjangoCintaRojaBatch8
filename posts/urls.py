from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^todos/$',
		views.PostView.as_view(),
		name="todos"),

	url(r'^detalle/(?P<matti>\d+)',
		views.PostDetailView.as_view(),
		name="detalle"),

	url(r'^api/$',
		views.Api.as_view(),
		name="api"),
	
]
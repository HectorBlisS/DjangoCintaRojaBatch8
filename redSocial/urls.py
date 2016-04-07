from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^cuentas/',
    	include('cuentas.urls',namespace="cuentas")),

    url(r'^posts/',
    	include('posts.urls',namespace="posts")),

    url('', include('social.apps.django_app.urls', namespace='social')),
    
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view='django.views.static.serve',
    	kwargs={'document_root':settings.MEDIA_ROOT}
    	),
   
    

    
]

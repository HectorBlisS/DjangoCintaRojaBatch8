from django.contrib import admin
from .models import Post, Comentario

class PostAdmin(admin.ModelAdmin):
	list_display=('titulo','slug','autor','fecha')
	list_filter=('fecha', 'autor')
	search_fields=('titulo','cuerpo')
	prepopulated_fields={'slug':('titulo',)}
	# date_hierarchy='fecha'
	ordering=['fecha']

admin.site.register(Post, PostAdmin)

class ComentarioAdmin(admin.ModelAdmin):
	list_display=('post','name','fecha')
	search_fields=('cuerpo',)

admin.site.register(Comentario, ComentarioAdmin)

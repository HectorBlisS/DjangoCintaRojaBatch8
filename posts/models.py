from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Post(models.Model):
	titulo=models.CharField(max_length=50)
	slug=models.SlugField(max_length=50, blank=True,null=True)
	cuerpo=models.TextField()
	fecha=models.DateTimeField(auto_now=True)
	publicado=models.BooleanField(default=True)
	autor=models.ForeignKey(User,related_name='posts_publicados',blank=True,null=True)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('posts:detalle',args=[self.pk])


class Comentario(models.Model):
	titulo=models.CharField(max_length=50)


# class Post(models.Model):
# 	titulo=models.CharField(max_length=50)
# 	cuerpo=models.TextField()
# 	fecha=models.DateTimeField(auto_now=True)
# 	publicado=models.BooleanField(default=True)

# 	def __str__(self):
# 		return self.titulo


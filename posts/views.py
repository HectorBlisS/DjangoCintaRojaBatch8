from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from django.views.generic import View
from .forms import PostForm, ComentarioForm

from django.core import serializers

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class PostView(View):
	def get(self,request):
		template="posts/todos.html"
		posts=Post.objects.all()
		form=PostForm()
		context={
		'posts':posts,
		'form':form
		}
		return render(request,template,context)
	def post(self, request):
		form=PostForm(request.POST)
		form.save()
		return redirect('posts:todos')

class PostDetailView(View):
	def get(self,request,matti):
		post=Post.objects.get(pk=matti)
		form=ComentarioForm()
		comments=post.comentarios.all()
		template="posts/detalle.html"
		context={
		'post':post,
		'form':form,
		'comments':comments
		}
		return render(request,template,context)

	def post(self,request,matti):
		post=Post.objects.get(pk=matti)
		new_form=ComentarioForm(request.POST)

		if new_form.is_valid():
			new_com=new_form.save(commit=False)
			new_com.name=request.user
			new_com.post=post
			new_com.save()
			messages.success(request,"Comentario agregado!")
		else:
			messages.error(request, 'Algo falló')
		return HttpResponseRedirect(reverse('posts:detalle',args=[matti]))


class Api(View):
	def get(self,request):
		posts=Post.objects.all()
		data=serializers.serialize('json',posts)
		return HttpResponse(data,content_type='application/json')




	# def post(self,request):
	# 	form=PostForm(request.POST)
	# 	form.save()
	# 	return redirect('todos')

		









# class PostView(View):
# 	def get(self,request):
# 		template="posts/todos.html"

# 		posts=Post.objects.all()
# 		context={
# 			'posts':posts
# 		}
# 		return render(request,template,context)


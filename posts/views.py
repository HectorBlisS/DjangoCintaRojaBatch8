from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from django.views.generic import View
from .forms import PostForm

from django.core import serializers


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
		template="posts/detalle.html"
		context={
		'post':post
		}
		return render(request,template,context)


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


from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm


# def news(request):
#     return render(request, 'lvlup/news.html')
#
#
# def upload(request):
#     return HttpResponse("Upload view")

class News(ListView):
    model = Post
    template_name = 'lvlup/news.html'
    ordering = ['-id']


class AddPost(CreateView):
    model = Post
    template_name = 'lvlup/add_post.html'
    form_class = PostForm
    # fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    template_name = 'lvlup/update_post.html'
    fields = ['title', 'body']


class DeletePost(DeleteView):
    model = Post
    template_name = 'lvlup/delete_post.html'
    success_url = reverse_lazy('news')

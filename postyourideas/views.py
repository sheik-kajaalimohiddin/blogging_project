from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
# Create your views here.


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'postyourideas/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'postyourideas/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'postyourideas/about.html',{'title':'About'})


def announcements(request):
    return render(request,'postyourideas/announcements.html',{'title':'Announcements'})


def calendars(request):
    return render(request,'postyourideas/calendars.html',{'title':'calendars'})


def etc(request):
    return render(request,'postyourideas/etc.html',{'title':'etc'})
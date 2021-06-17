from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
	queryset = Post.objects.order_by('-created_on')
	model = Post
	template_name ='home.html'
	paginate_by = 5
	
class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

def AboutDetailView(request):
	return render(request, 'about_details.html')
	
class MyListView(ListView):
	model = Post
	template_name = 'list_details.html'

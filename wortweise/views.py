from django.shortcuts import render
from django import forms
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
class HomeView(ListView):
	queryset = Post.objects.order_by('-created_on')
	model = Post
	template_name ='home.html'
	paginate_by = 5
	
def post_detail(request, slug):
    template_name = 'article_details.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
def AboutDetailView(request):
	return render(request, 'about_details.html')

def ContactDetailView(request):
	return render(request, 'contact_details.html')
	
class MyListView(ListView):
	model = Post
	template_name = 'list_details.html'



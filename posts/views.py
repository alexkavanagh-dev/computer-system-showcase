from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    querySet = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


def add_post(request):

    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)

        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            post_form.instance.email = request.user.email
            post_form.instance.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return redirect(reverse('home'))
        else:
            print(post_form.errors)
            post_form = PostForm()

    else:
        post_form = PostForm()

    return render(request, 'add_post.html', {"post_form": post_form})

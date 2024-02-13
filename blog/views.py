from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event


def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "coder": "Matt Rudge"},
    )



    return render(
        request,
       "events/event_detail.html",
        {"event": event}
    )
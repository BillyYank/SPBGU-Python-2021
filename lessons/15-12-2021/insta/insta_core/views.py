from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from friendship.models import Friend, Follow, Block

# Create your views here.


def main_page(request):
    return render(request, 'insta_core/main.html')


def feed(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'insta_core/feed.html', context={'posts': posts})
    else:
        return HttpResponse(status=404)


class ProfileView(TemplateView):
    template_name = "insta_core/profile.html"

    def get(self, request, profile_id, *args):
        profile = Profile.objects.get(pk=profile_id)
        return render(request, self.template_name, context={'profile': profile})

    def post(self, request, user_id, *args):
        return HttpResponse(status=404) #redirect(f'/api/v0/user/{request.user.id}')


def subscribe(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    follow = Follow.objects.add_follower(request.user, profile.user)
    return redirect('profile', profile_id=profile.id)
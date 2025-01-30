from django.shortcuts import render
from user.models import CustomUser


def home_screen_view(request):
    return render(request, 'home.html')


def get_users(requests):
    context = {}
    users = CustomUser.objects.all()
    context['users'] = users
    return render(requests, 'users.html', context)

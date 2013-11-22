# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from register.models import User

def index(request):
    return render(request, 'register/index.html', {})

def done(request):
    if User.objects.filter(username = request.POST['username']):
        return HttpResponseRedirect(reverse('register:index'))
    else:
        u = User(username=request.POST['username'],
             password=request.POST['password'],
             nickname=request.POST['nickname'])
        u.save()
        print u
        return render(request, 'register/done.html', {})

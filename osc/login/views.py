# Create your views here.
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from register.models import User

def index(request):
    return render(request, 'login/index.html', {})

def done(request):
    u = User.objects.filter(username = request.POST['username'])
    print request.POST['password'], u[0].password
    if u and request.POST['password'] == u[0].password:
        return render(request, 'login/done.html', {})
    else:
        return HttpResponseRedirect(reverse('login:index'))

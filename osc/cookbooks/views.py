# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from cookbooks.models import blog
from django.core.urlresolvers import reverse
def index(request):
    return render(request, 'cookbooks/cookbook.html', {'l': blog.objects.all()})

def newcb(request):
    return render(request, 'cookbooks/newcb.html', {})

def submitncb(request):
    try:
        b = blog(title = request.POST['title'], content = request.POST['content'])
    except (KeyError):
        # Redisplay the poll voting form.
        print 1
    else:
        b.save()
    return HttpResponseRedirect(reverse('cookbooks:index'))

def blogarticle(request, blog_id):
    b = blog.objects.get(id=blog_id)
    return render(request, 'cookbooks/blog.html', {'b': b})

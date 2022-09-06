from django.shortcuts import render
from .models import ShortURLS
from .forms import ShortenerForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
# from django.http import HttpResponseNotFound
from django.contrib.auth.models import User

def homePage(request):
    template = 'home.html'
    context = {}
    # Empty form
    context['form'] = ShortenerForm()
    if request.method == 'GET':
        return render(request, template, context)
    
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save(commit=False)
            if request.user.is_authenticated:
                shortened_object.user = request.user 
            shortened_object.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['new_url']  = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = ShortURLS.objects.filter(is_deleted=False).get(short_url=shortened_part)
        # shortener.times_followed += 1        
        # shortener.save()
        return HttpResponseRedirect(shortener.long_url) 
    except:
        return HttpResponse('Sorry this link is broken :(')

from django.http import HttpResponse
from django.shortcuts import render,redirect
from myapp.models import *



def show_about_page(request):
    print('about page')
    name = 'learcodewith durgesh'
    link = 'http://www.youtube.com'
    data = {
        'name': name,
        'link': link
    }
    return render(request, 'about.html', data)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images, 'cats': cats}
    return render(request, "home.html", data)

def show_category_page(request, cid):
    cats = Category.objects.all()

    cat = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=cat)
    data = {'images': images, 'cats': cats}
    return render(request, "home.html", data)

def home(request):
    return redirect('/home')
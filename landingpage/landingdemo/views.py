from django.shortcuts import render
from landingdemo.models import PersonalBlog


def home(request):
    context = {}
    template = 'alltemplates/home.html'
    return render(request, template, context)


def bioPage(request):
    context = {}
    template = 'alltemplates/bio.html'
    return render(request, template, context)


def editingPage(request):
    context = {}
    template = 'alltemplates/editing.html'
    return render(request, template, context)


def weldingPage(request):
    context = {}
    template = 'alltemplates/welding.html'
    return render(request, template, context)


def drinkPage(request):
    context = {}
    template = 'alltemplates/drink.html'
    return render(request, template, context)


def actualBlogPage(request):
    context = {}
    template = 'alltemplates/actual_blog.html'
    return render(request, template, context)


def blogPage(request):
    blogs = PersonalBlog.objects.all()
    context = {'blogs': blogs}
    template = 'alltemplates/blog.html'
    return render(request, template, context)
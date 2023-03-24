from django.shortcuts import render


def home(request):
    context = {}
    template = 'comingsoon/home.html'
    return render(request, template, context)


def bioPage(request):
    context = {}
    template = 'comingsoon/bio.html'
    return render(request, template, context)


def editingPage(request):
    context = {}
    template = 'comingsoon/editing.html'
    return render(request, template, context)


def weldingPage(request):
    context = {}
    template = 'comingsoon/welding.html'
    return render(request, template, context)

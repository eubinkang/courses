from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
    'classes' : Course.objects.all()
    }
    return render(request, "course/index.html", context)

def course(request):
    context = {
    'classes' : Course.objects.all()
    }

    if request.method == 'POST':
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])

        return redirect('/')

def destroy(request, id):
    course = Course.objects.get(id = id)
    context = {'course': course}
    if request.method == "POST":
        if request.POST['submit'] == "Yes":
            Course.objects.filter(id=id).delete()
            return redirect('/')
    else:
        return render(request, 'course/destroy.html', context)

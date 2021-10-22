from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'template.html')

def bienvenidos(request):
    return render(request,'bienvenidos.html')



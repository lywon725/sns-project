from django.shortcuts import render

# Create your views here.

def showmain(request):
    return render(request, 'main/mainpage.html')

def first(request):
    return render(request, 'main/first.html')

def second(request):
    return render(request, 'main/second.html')

def photo1(request):
    return render(request, 'main/photo_1.html')
def photo2(request):
    return render(request, 'main/photo_2.html')
def photo3(request):
    return render(request, 'main/photo_3.html')
def photo4(request):
    return render(request, 'main/photo_4.html')
def photo5(request):
    return render(request, 'main/photo_5.html')
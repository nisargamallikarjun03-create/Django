from django.shortcuts import render

def student(request):
    return render(request, 'student.html')

def january(request):
    return render(request, 'january.html')
def feb(request):
    return render(request, 'feb.html')
def march(request):
    return render(request, 'march.html')
def intro(request):
    return render(request, 'intro.html')
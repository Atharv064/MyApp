from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    isActive = True
    if request.method == 'POST':
        check = request.POST.get('check')
        print(check)
        if check is not None:
            isActive = False
        else:
            isActive = True

    name = "Atharv Desai"
    list_of_programs = [
        'WAP to check odd or even',
        'WAP to check palindrome',
        'WAP to print all the prime numbers',
        'WAP to print pascals traingle',
    ]
    student={
        'student_name' : "Rahul",
        'student_college' : 'zyz',
        'student_city' : 'Lucknow',
    }

    #return HttpResponse("<h1>Hello this is index page</h1>")
    data = {
            'isActive':isActive,
            'name':name,
            'list_of_programs':list_of_programs,
            'student_data':student,
    }
    return render(request, "home.html", data)

def about(request):
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html", {})

def services(request):
    #return HttpResponse("<h1>This is services page</h1>")
    return render(request, "services.html", {})

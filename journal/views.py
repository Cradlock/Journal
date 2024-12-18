from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from .models import *



def index(request):
    students = Student.objects.all()

    if request.method == 'POST':
        search_data = request.POST.get('data', '').strip()

        filtered_students = students.none()

        try:
            filtered_students = students.filter(number=search_data)
        except ValueError:
            pass


        if not filtered_students:
            filtered_students = students.filter(name__icontains=search_data)


        if not filtered_students:
            filtered_students = students.filter(surname__icontains=search_data)

        students = filtered_students

    context = {
        "title":"Главная страница",
        "students":students,
    }
    return render(request,"index.html",context)


def rating(request):
    students_sort = None
    if request.method == "GET":
        point_f = request.GET.get("points")
        truancies_f = request.GET.get("truancies_not_cause")
        truancies_c = request.GET.get("truancies_cause")



        if point_f:
            students = Student.objects.all().order_by("point")
            for i,item in enumerate(students):
                item.place_rating = i+1
            students_sort = students
        elif truancies_f:
            students = Student.sorted_by_truancy_count()
            for i, item in enumerate(students):
                item.place_rating = i + 1
            students_sort = students
        elif truancies_c:
            students = Student.objects.annotate(truancies=Count("truancie")).order_by("truancie")
            for i, item in enumerate(students):
                item.place_rating = i + 1
            students_sort = students

    context = {
        "title":"Рейтинг",
        "students":students_sort
    }
    return render(request,"rating.html",context)

def student(request,id):
    try:
        people = Student.objects.get(id=id)
        truiances = Truancie.objects.filter(student=people)
    except:
        return redirect('404')

    if request.method == 'POST' and request.user.is_authenticated and request.user.is_staff:
        grade = request.POST.get('grade')
        try:
           people.point += int(grade)
           people.save()
        except:
            pass



    context = {
        "title":f"{people.name}  {people.surname}",
        "student":people,
        "truiances":truiances,
        "count":truiances.count()
    }
    return render(request,"student.html",context)

def rules(request):
    rules_list = Rules.objects.all().last()
    context = {
       "data":rules_list
    }
    return render(request,"rules.html",context=context)

def page404(request,**kwargs):
    context = {
        "title":"Страница не найдена"
    }
    return render(request,"404.html",context)


def loginF(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            messages.error(request,"Неверное имя пользователя или пароль")

    context = {
        "title": "Авторизация",
        "isLogin":True
    }
    return render(request, "login.html", context)


def logoutF(request):
    logout(request)
    return redirect("index")
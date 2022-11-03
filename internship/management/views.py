from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        
        loginprn = request.POST['prn']

        loginpass = request.POST['pass']

        user = Login.objects.filter(Loginid=loginprn, Password=loginpass)



        if user.exists():
            supervi = CollegeSuper.objects.filter(CO_prn=loginprn)
            student=Student.objects.filter(S_prn=loginprn)
            comp=company.objects.filter(C_email=loginprn)
            if supervi.exists():
                for i in supervi:
                    a = i.Co_id
                students = Student.objects.filter(SCO_id=a)
                teacher = i
                return render(request, 'home.html', {'stu': students , 'teacher' : teacher})
            elif student.exists():
                for i in student:
                    b=i.S_id
                stu=Student.objects.get(S_id=b) 
                return render(request,"studet.html", {'stu': stu})
            elif comp.exists():
                for i in comp:
                    c=i.C_id
                det=Student.objects.filter(SC_id=c)
                supervisor = i
                return render(request,"compdash.html",{'stu': det, 'supervisor' : supervisor})
        else:
            return redirect('login')
    return render(request, 'login.html')



def details(request, id):
    detai = Student.objects.get(S_id=id)
    midTermForm = mideterm.objects.filter(SM = id)
    endTermForm = Endterm.objects.filter(SE = id)
    return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

def cdetails(request, id):
    detai = Student.objects.get(S_id=id)
    midTermForm = Cmideterm.objects.filter(C_SM = id)
    endTermForm = CEndterm.objects.filter(C_SE = id)
    return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

def midterm(request, id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')
        mark7 = request.POST.get('mark7')

        sub = mideterm(domainandtech=mark1,
                       presentation=mark2,
                       taskcompleted=mark3,
                       communication=mark4,
                       interpersonatl=mark5,
                       profesethi=mark6,
                       questionans=mark7,
                       total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5)+int(mark6)+int(mark7),
                       SM_id=id)

        sub.save()
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id)
        endTermForm = Endterm.objects.filter(SE = id)
        return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    mid = mideterm.objects.filter(SM_id=id)
    if mid.exists():
        form = mideterm.objects.get(SM = id)
        student = Student.objects.get(S_id = id)
        return render(request, 'midform.html', {'form' : form, 'student': student})
    else:
        student = Student.objects.get(S_id=id)
        return render(request, 'midformdet.html', {'student': student})
    
    
def cmidterm(request, id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')
        mark7 = request.POST.get('mark7')

        sub = Cmideterm(C_domainandtech=mark1,
                       C_presentation=mark2,
                       C_taskcompleted=mark3,
                       C_communication=mark4,
                       C_interpersonatl=mark5,
                       C_profesethi=mark6,
                       C_questionans=mark7,
                       C_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5)+int(mark6)+int(mark7),
                       C_SM_id=id)

        sub.save()
        detai = Student.objects.get(S_id=id)
        midTermForm = Cmideterm.objects.filter(C_SM = id)
        endTermForm = CEndterm.objects.filter(C_SE = id)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    mid = Cmideterm.objects.filter(C_SM_id=id)
    if mid.exists():
        form = Cmideterm.objects.get(C_SM = id)
        student = Student.objects.get(S_id = id)
        return render(request, 'cmidform.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'cmidformdet.html', {'student': student})



def endterm(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')
        mark7 = request.POST.get('mark7')
        mark8 = request.POST.get('mark8')
        mark9 = request.POST.get('mark9')
        mark10 = request.POST.get('mark10')

        sub = Endterm(background=mark1,
                       scopeandobj=mark2,
                       implemen=mark3,
                       observa=mark4,
                       domain=mark5,
                      present=mark6,
                       communic=mark7,
                       interper=mark8,
                       profess=mark9,
                        qanda=mark10,
                       E_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5)+int(mark6)+int(mark7)+int(mark8)+int(mark9)+int(mark10),
                       SE_id=id)

        sub.save()
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id)
        endTermForm = Endterm.objects.filter(SE = id)
        return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    end = Endterm.objects.filter(SE_id=id)
    if end.exists():
        form = Endterm.objects.get(SE = id)
        student = Student.objects.get(S_id = id)
        return render(request, 'endform.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'endformdet.html', {'student': student})

def cendterm(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')
        mark7 = request.POST.get('mark7')
        mark8 = request.POST.get('mark8')
        mark9 = request.POST.get('mark9')
        mark10 = request.POST.get('mark10')

        sub = CEndterm(C_background=mark1,
                       C_scopeandobj=mark2,
                       C_implemen=mark3,
                       C_observa=mark4,
                       C_domain=mark5,
                       C_present=mark6,
                       C_communic=mark7,
                       C_interper=mark8,
                       C_profess=mark9,
                        C_qanda=mark10,
                       C_E_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5)+int(mark6)+int(mark7)+int(mark8)+int(mark9)+int(mark10),
                       C_SE_id=id)

        sub.save()
        detai = Student.objects.get(S_id=id)
        midTermForm = Cmideterm.objects.filter(C_SM = id)
        endTermForm = CEndterm.objects.filter(C_SE = id)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    end = CEndterm.objects.filter(C_SE_id=id)
    if end.exists():
        form = CEndterm.objects.get(C_SE = id)
        student = Student.objects.get(S_id = id)
        return render(request, 'cendform.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'cendformdet.html', {'student': student})

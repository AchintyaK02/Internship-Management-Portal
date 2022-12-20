from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
from .models import *
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os 

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
            comp=compper.objects.filter(P_email=loginprn)
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
                    c=i.P_id
                    j=i.P_fname+" "+i.P_lname
                det=Student.objects.filter(SC_id=c)
                supervisor = j
                return render(request,"compdash.html",{'stu': det, 'supervisor' : supervisor,'com':comp})
        else:
            return redirect('login')
    return render(request, 'login.html')



def details(request, id):
    student = Student.objects.get(S_id=id)
    field_name = 'comper'
    field_object = Student._meta.get_field(field_name)
    field_value = field_object.value_from_object(student)
    company_person = compper.objects.get(P_id = field_value)
    midTermForm = mideterm.objects.filter(SM=id, SF=1)
    endTermForm = Endterm.objects.filter(SE=id,SEF=1)
    Compform=comeval.objects.filter(CE=id,CEF=1)
    ProgressForm = progresseval.objects.filter(PE_id=id,PEF_id=1)
    return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : 
    endTermForm,'Compform':Compform,'Progressform':ProgressForm})

def cdetails(request, id):
    detai = Student.objects.get(S_id=id)
    midTermForm = mideterm.objects.filter(SM = id,SF=2)
    endTermForm = Endterm.objects.filter(SE =id,SEF=2)
    Compform=comeval.objects.filter(CE=id)
    ProgressForm = progresseval.objects.filter(PE_id=id,PEF_id=2)
    return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : 
    endTermForm,'Compform':Compform,'Progressform':ProgressForm})

def midterm(request, id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
       
        sub = mideterm(domainandtech=mark1,
                       presentation=mark2,
                       communication=mark3,
                       questionans=mark4,
                       total=int(mark1)+int(mark2)+int(mark3)+int(mark4),
                       SM_id=id,SF_id=1)

        sub.save()
        Student.objects.filter(S_id=id).update(S_m=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=1)
        endTermForm = Endterm.objects.filter(SE = id,SEF=1)
        return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    mid = mideterm.objects.filter(SM_id=id,SF_id=1)
    if mid.exists():
        form = mideterm.objects.get(SM = id,SF_id=1)
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
       
        sub = mideterm(domainandtech=mark1,
                       presentation=mark2,
                       communication=mark3,
                       questionans=mark4,
                       total=int(mark1)+int(mark2)+int(mark3)+int(mark4),
                       SM_id=id,SF_id=2)

        sub.save()
        Student.objects.filter(S_id=id).update(S_cm=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=2)
        endTermForm = Endterm.objects.filter(SE = id,SEF=2)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    mid = mideterm.objects.filter(SM=id,SF=2)
    if mid.exists():
        form = mideterm.objects.get(SM = id,SF=2)
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
       
        sub = Endterm(
                       
                       implemen=mark1,
                       observa=mark2,
                       present=mark3,
                       communic=mark4,
                       qanda=mark5,
                       E_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5),
                       SE_id=id,SEF_id=1)

        sub.save()
        Student.objects.filter(S_id=id).update(S_e=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=1)
        endTermForm = Endterm.objects.filter(SE = id,SEF=1)
        return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    end = Endterm.objects.filter(SE_id=id,SEF=1)
    if end.exists():
        form = Endterm.objects.get(SE = id,SEF=1)
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
       
        sub = Endterm(
                       
                       implemen=mark1,
                       observa=mark2,
                       present=mark3,
                       communic=mark4,
                       qanda=mark5,
                       E_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5),
                       SE_id=id,SEF_id=2)

        sub.save()
        Student.objects.filter(S_id=id).update(S_ce=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=1)
        endTermForm = Endterm.objects.filter(SE = id,SEF=1)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm})

    end = Endterm.objects.filter(SE=id,SEF=2)
    if end.exists():
        form = Endterm.objects.get(SE = id,SEF=2)
        student = Student.objects.get(S_id = id)
        return render(request, 'cendform.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'cendformdet.html', {'student': student})


def goback(request,id):
    teacher = CollegeSuper.objects.get(Co_id=id)
    students = Student.objects.filter(SCO_id=id)
    return render(request, 'home.html', {'stu': students , 'teacher' : teacher})

def cgoback(request,id):
    sup = compper.objects.get(P_id=id)
    supp=sup.P_fname+" "+sup.P_lname
    students = Student.objects.filter(comper_id=id)
    return render(request, 'compdash.html', {'supervisor': supp , 'stu' : students})

def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='appliccation/pdf')
    return None

def mrepo(request,id,*args,**kwargs):
    try:
        tmid=mideterm.objects.filter(SM = id)
        cmid = mideterm.objects.filter(C_SM = id)
    except:
        return HttpResponse("505 NOT FOUND")
    
    student = Student.objects.get(S_id = id)

    for i in tmid:
        a=i.domainandtech
        b=i.presentation
        c=i.taskcompleted
        d=i.communication
        e=i.interpersonatl
        f=i.profesethi
        g=i.questionans

    for j in cmid:
        h=j.C_domainandtech
        m=j.C_presentation
        n=j.C_taskcompleted
        o=j.C_communication
        p=j.C_interpersonatl
        q=j.C_profesethi
        r=j.C_questionans

    data={
        'mark1':int(a)+int(h),
        'mark2':int(b)+ int(m),
        'mark3':int(c)+ int(n),
        'mark4':int(d)+ int(o),
        'mark5':int(e)+ int(p),
        'mark6':int(f)+ int(q),
        'mark7':int(g)+ int(r),
        'student' : student
    }  
    pdf =render_to_pdf('mreport.html',data)
    return HttpResponse(pdf,content_type='application/pdf')


def erepo(request,id,*args,**kwargs):
    try:
        tmid=Endterm.objects.filter(SE = id)
        cmid = Endterm.objects.filter(C_SE = id)
    except:
        return HttpResponse("505 NOT FOUND")

    student = Student.objects.get(S_id = id)

    for i in tmid:
        a=i.background
        b=i.scopeandobj
        c=i.implemen
        d=i.observa
        e=i.domain
        f=i.present
        g=i.communic
        s=i.interper
        t=i.profess
        u=i.qanda


    for j in cmid:
        h=j.C_background
        m=j.C_scopeandobj  
        n=j.C_implemen
        o=j.C_observa 
        p=j.C_domain
        q=j.C_present  
        r=j.C_communic
        v=j.C_interper
        w=j.C_profess
        x=j.C_qanda

    data={
        'mark1':int(a)+int(h),
        'mark2':int(b)+ int(m),
        'mark3':int(c)+ int(n),
        'mark4':int(d)+ int(o),
        'mark5':int(e)+ int(p),
        'mark6':int(f)+ int(q),
        'mark7':int(g)+ int(r),
        'mark8':int(s)+ int(v),
        'mark9':int(t)+ int(w),
        'mark10':int(u)+int(x),
        'student' : student
    }  
    pdf =render_to_pdf('ereport.html',data)
    return HttpResponse(pdf,content_type='application/pdf')



def Compform(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
       
        sub = comeval(
                       
                       problem=mark1,
                       collect=mark2,
                       Team=mark3,
                       oralwrit=mark4,
                       punctuality=mark5,
                       CE_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5),
                       CE_id=id,CEF_id=2)

        sub.save()
        Student.objects.filter(S_id=id).update(CE_C=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=1)
        endTermForm = Endterm.objects.filter(SE = id,SEF=1)
        Compform=comeval.objects.filter(CE_id=id)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm,'Compform':Compform})

    Comp = comeval.objects.filter(CE=id)
    if Comp.exists():
        form = comeval.objects.get(CE_id = id)
        student = Student.objects.get(S_id = id)
        return render(request, 'ccomform.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'ccomformdet.html', {'student': student})



def SCompform(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
       
        # sub = comeval(
                       
        #                problem=mark1,
        #                collect=mark2,
        #                Team=mark3,
        #                oralwrit=mark4,
        #                punctuality=mark5,
        #                CE_total=int(mark1)+int(mark2)+int(mark3) +
        #                int(mark4)+int(mark5),
        #                CE=id,CEF=2)

        # sub.save()
        
         
        comeval.objects.filter(CE_id=id).update(CEF_id=1,problem=mark1,collect=mark2,Team=mark3,oralwrit=mark4,punctuality=mark5, 
        CE_total=int(mark1)+int(mark2)+int(mark3) +int(mark4)+int(mark5))
        Student.objects.filter(S_id=id).update(CE_S=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=1)
        endTermForm = Endterm.objects.filter(SE = id,SEF=1)
        Compform=comeval.objects.filter(CE_id=id,CEF_id=1)
        return render(request, 'details.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : endTermForm,'Compform':Compform})

    Comp = comeval.objects.filter(CE=id,CEF_id=2)
    Comp1=comeval.objects.filter(CE=id,CEF_id=1)
    if Comp.exists():
        form = comeval.objects.get(CE_id = id)
        student = Student.objects.get(S_id = id)
        return render(request, 'Scomformdet.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'ccomform.html', {'student': student,'Compform':Comp1})


def Sprogresseval(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
       
       
        sub = progresseval(
                       
                       Taskperfo=mark1,
                       workcomplete=mark2,
                       Weekreport=mark3,
                       repowrit=mark4,
                       
                       PE_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4),
                       PE_id=id,PEF_id=1)

        sub.save()
        Student.objects.filter(S_id=id).update(PE_S=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=1)
        endTermForm = Endterm.objects.filter(SE = id,SEF=1)
        Compform=comeval.objects.filter(CE_id=id)
        Progress=progresseval.objects.filter(PE_id=id,PEF_id=1)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : 
        endTermForm,'Compform':Compform,'Progresseval':Progress})

    Comp = progresseval.objects.filter(PE_id=id,PEF_id=1)
    if Comp.exists():
        form = progresseval.objects.get(PE_id = id,PEF_id=1)
        student = Student.objects.get(S_id = id)
        return render(request, 'progresseval.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'progevaldet.html', {'student': student})


def Cprogresseval(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
       
       
        sub = progresseval(
                       
                       Taskperfo=mark1,
                       workcomplete=mark2,
                       Weekreport=mark3,
                       repowrit=mark4,
                       
                       PE_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4),
                       PE_id=id,PEF_id=1)

        sub.save()
        Student.objects.filter(S_id=id).update(PE_C=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM = id,SF=2)
        endTermForm = Endterm.objects.filter(SE = id,SEF=2)
        Compform=comeval.objects.filter(CE_id=id)
        Progress=progresseval.objects.filter(PE_id=id,PEF_id=2)
        return render(request, 'cdetails.html', {'det': detai , 'midTermForm' : midTermForm, 'endTermForm' : 
        endTermForm,'Compform':Compform,'Progresseval':Progress})

    Comp = progresseval.objects.filter(PE_id=id,PEF_id=2)
    if Comp.exists():
        form = progresseval.objects.get(PE_id = id,PEF_id=2)
        student = Student.objects.get(S_id = id)
        return render(request, 'progresseval.html', {'form' : form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'progevaldet.html', {'student': student})





    


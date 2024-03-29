from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Sum
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
            student = Student.objects.filter(S_prn=loginprn)
            comp = compper.objects.filter(P_email=loginprn)
            if supervi.exists():
                for i in supervi:
                    a = i.Co_id
                students = Student.objects.filter(SCO_id=a)
                t=Student.objects.filter(SCO_id=a).count()
                m=Student.objects.filter(SCO_id=a,S_m=True).count()
                e=Student.objects.filter(SCO_id=a,S_e=True).count()
                q=Student.objects.filter(SCO_id=a,CE_S=True).count()
                p=Student.objects.filter(SCO_id=a,PE_S=True).count()
                print(e)
                m=round(m/t*100)
                e=round(e/t*100)
                q=round(q/t*100)
                p=round(p/t*100)
                teacher = i
                return render(request, 'home.html', {'stu': students, 'teacher': teacher,'mid':m,'end':e,'ce':q,'pe':p})
            elif student.exists():
                for i in student:
                    b = i.S_id
                stu = Student.objects.get(S_id=b)
                return render(request, "studet.html", {'stu': stu})
            elif comp.exists():
                for i in comp:
                    c = i.P_id
                det = Student.objects.filter(comper_id=c)
                supervisor = i
                t=Student.objects.filter(comper_id=c).count()
                m=Student.objects.filter(comper_id=c,S_cm=True).count()
                e=Student.objects.filter(comper_id=c,S_ce=True).count()
                q=Student.objects.filter(comper_id=c,CE_C=True).count()
                p=Student.objects.filter(comper_id=c,PE_C=True).count()
                m=round(m/t*100)
                e=round(e/t*100)
                q=round(q/t*100)
                p=round(p/t*100)
                
                return render(request, "compdash.html", {'stu': det, 'supervisor': supervisor, 'com': comp,'id':c,'mid':m,'end':e,'ce':q,'pe':p})
        else:
            return redirect('login')
    return render(request, 'login.html')


def details(request, id):
    student = Student.objects.get(S_id=id)
    field_name = 'comper'
    field_object = Student._meta.get_field(field_name)
    field_value = field_object.value_from_object(student)
    company_person = compper.objects.get(P_id=field_value)
    midTermForm = mideterm.objects.filter(SM=id, SF=1)
    endTermForm = Endterm.objects.filter(SE=id,SEF=1)
    Compform=comeval.objects.filter(CE=id,CEF=1)
    ProgressForm = progresseval.objects.filter(PE_id=id,PEF=1)
    return render(request, 'details.html', {'com':company_person ,'det': student , 'midTermForm' : midTermForm, 'endTermForm' : 
    endTermForm,'Compform':Compform,'Progressform':ProgressForm})

def cdetails(request, id):
    student = Student.objects.get(S_id=id)
    field_name = 'SCO'
    field_object = Student._meta.get_field(field_name)
    field_value = field_object.value_from_object(student)
    college_supervisor = CollegeSuper.objects.get(Co_id = field_value)
    midTermForm = mideterm.objects.filter(SM = id,SF=2)
    endTermForm = Endterm.objects.filter(SE =id,SEF=2)
    Compform=comeval.objects.filter(CE=id)
    ProgressForm = progresseval.objects.filter(PE_id=id,PEF=2)
    return render(request, 'cdetails.html', { 'com' : college_supervisor , 'det': student , 'midTermForm' : midTermForm, 'endTermForm' : 
    endTermForm,'Compform':Compform,'ProgressForm':ProgressForm})

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
                       SM_id=id, SF=1)

        sub.save()
        Student.objects.filter(S_id=id).update(S_m=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=1)
        endTermForm = Endterm.objects.filter(SE=id, SEF=1)
        Compform=comeval.objects.filter(CE=id,CEF=1)
        ProgressForm = progresseval.objects.filter(PE_id=id,PEF=1)
        return render(request, 'details.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm': 
        endTermForm,'Compform':Compform,'Progressform':ProgressForm})

    mid = mideterm.objects.filter(SM_id=id, SF=1)
    if mid.exists():
        form = mideterm.objects.get(SM=id, SF=1)
        student = Student.objects.get(S_id=id)
        return render(request, 'midform.html', {'form': form, 'student': student})
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
                       SM_id=id, SF=2)

        sub.save()
        Student.objects.filter(S_id=id).update(S_cm=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=2)
        endTermForm = Endterm.objects.filter(SE=id, SEF=2)
        Compform=comeval.objects.filter(CE=id)
        ProgressForm = progresseval.objects.filter(PE_id=id,PEF=2)

        return render(request, 'cdetails.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm': 
        endTermForm,'Compform':Compform,'Progressform':ProgressForm})

    mid = mideterm.objects.filter(SM=id, SF=2)
    if mid.exists():
        form = mideterm.objects.get(SM=id, SF=2)
        student = Student.objects.get(S_id=id)
        return render(request, 'cmidform.html', {'form': form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'cmidformdet.html', {'student': student})


def endterm(request, id):
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
            SE_id=id, SEF=1)

        sub.save()
        Student.objects.filter(S_id=id).update(S_e=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=1)
        endTermForm = Endterm.objects.filter(SE=id, SEF=1)
        Compform=comeval.objects.filter(CE=id,CEF=1)
        ProgressForm = progresseval.objects.filter(PE_id=id,PEF=1)
        return render(request, 'details.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm': 
         endTermForm,'Compform':Compform,'Progressform':ProgressForm})

    end = Endterm.objects.filter(SE_id=id, SEF=1)
    if end.exists():
        form = Endterm.objects.get(SE=id, SEF=1)
        student = Student.objects.get(S_id=id)
        return render(request, 'endform.html', {'form': form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'endformdet.html', {'student': student})


def cendterm(request, id):
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
            SE_id=id, SEF=2)

        sub.save()
        Student.objects.filter(S_id=id).update(S_ce=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=2)
        endTermForm = Endterm.objects.filter(SE=id, SEF=2)
        Compform=comeval.objects.filter(CE=id)
        ProgressForm = progresseval.objects.filter(PE_id=id,PEF=2)
        return render(request, 'cdetails.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm': 
         endTermForm,'Compform':Compform,'ProgressForm':ProgressForm})

    end = Endterm.objects.filter(SE=id, SEF=2)
    if end.exists():
        form = Endterm.objects.get(SE=id, SEF=2)
        student = Student.objects.get(S_id=id)
        return render(request, 'cendform.html', {'form': form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'cendformdet.html', {'student': student})


def goback(request, id):
    teacher = CollegeSuper.objects.get(Co_id=id)
    students = Student.objects.filter(SCO_id=id)
    t=Student.objects.filter(SCO_id=id).count()
    m=Student.objects.filter(SCO_id=id,S_m=True).count()
    e=Student.objects.filter(SCO_id=id,S_e=True).count()
    q=Student.objects.filter(SCO_id=id,CE_S=True).count()
    p=Student.objects.filter(SCO_id=id,PE_S=True).count()
    m=round(m/t*100)
    e=round(e/t*100)
    q=round(q/t*100)
    p=round(p/t*100)
    return render(request, 'home.html', {'stu': students, 'teacher': teacher,'mid':m,'end':e,'ce':q,'pe':p})


def cgoback(request, id):
    sup = compper.objects.get(P_id=id)
    id=sup.P_id
    supp = sup.P_fname+" "+sup.P_lname
    students = Student.objects.filter(comper_id=id)
    t=Student.objects.filter(comper_id=id).count()
    m=Student.objects.filter(comper_id=id,S_cm=True).count()
    e=Student.objects.filter(comper_id=id,S_ce=True).count()
    q=Student.objects.filter(comper_id=id,CE_C=True).count()
    p=Student.objects.filter(comper_id=id,PE_C=True).count()
    m=round(m/t*100)
    e=round(e/t*100)
    q=round(q/t*100)
    p=round(p/t*100)
    return render(request, 'compdash.html', {'supervisor_name' : supp, 'supervisor': sup, 'stu': students,'id':id,'mid':m,'end':e,'ce':q,'pe':p})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='appliccation/pdf')
    return None


def mrepo(request, id, *args, **kwargs):
    try:
        tmid = mideterm.objects.filter(SM_id=id).aggregate(Sum('domainandtech'), Sum(
            'presentation'), Sum('communication'), Sum('questionans'), Sum('total'))
        print(tmid)
        tend = Endterm.objects.filter(SE_id=id).aggregate(Sum('implemen'), Sum(
            'observa'), Sum('present'), Sum('communic'), Sum('qanda'), Sum("E_total"))
        print(tend)
        tcomev = comeval.objects.filter(CE_id=id).aggregate(Sum('problem'), Sum(
            'collect'), Sum('Team'), Sum('oralwrit'), Sum('punctuality'), Sum('CE_total'))
        print(tcomev)
        tproeva = progresseval.objects.filter(PE_id=id).aggregate(Sum('Taskperfo'), Sum(
            'workcomplete'), Sum('Weekreport'), Sum('repowrit'), Sum('PE_total'))
        print(tproeva)
        # cmid = Cmideterm.objects.filter(C_SM=id)
    except:
        return HttpResponse("505 NOT FOUND")

    student = Student.objects.get(S_id=id)

    data = {
        'mid': tmid,
        'end': tend,
        'comp': tcomev,
        'progev': tproeva,
        'student': student,
    }
    pdf = render_to_pdf('mreport.html', data)
    return HttpResponse(pdf, content_type='application/pdf')



def Compform(request, id):
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
            CE_id=id, CEF=2)

        sub.save()
        Student.objects.filter(S_id=id).update(CE_C=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=2)
        endTermForm = Endterm.objects.filter(SE=id, SEF=2)
        Compform = comeval.objects.filter(CE_id=id)
        Progress = progresseval.objects.filter(PE_id=id, PEF=2)
        return render(request, 'cdetails.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm': endTermForm, 'Compform': 
        Compform,'ProgressForm': Progress})

    Comp = comeval.objects.filter(CE=id)
    if Comp.exists():
        form = comeval.objects.get(CE_id=id)
        student = Student.objects.get(S_id=id)
        return render(request, 'ccomform.html', {'form': form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'ccomformdet.html', {'student': student})


def SCompform(request, id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')

        comeval.objects.filter(CE_id=id).update(CEF=1, problem=mark1, collect=mark2, Team=mark3, oralwrit=mark4, punctuality=mark5,
                                                CE_total=int(mark1)+int(mark2)+int(mark3) + int(mark4)+int(mark5))
        Student.objects.filter(S_id=id).update(CE_S=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=1)
        endTermForm = Endterm.objects.filter(SE=id, SEF=1)
        Compform = comeval.objects.filter(CE_id=id, CEF=1)
        progress=progresseval.objects.filter(PE_id=id,PEF=1)
        return render(request, 'details.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm': endTermForm, 'Compform': 
        Compform,'Progressform': progress})

    Comp = comeval.objects.filter(CE=id, CEF=2)
    Comp1 = comeval.objects.filter(CE=id, CEF=1)

    if Comp.exists():
        form = comeval.objects.get(CE_id=id)
        student = Student.objects.get(S_id=id)
        return render(request, 'scomformdet.html', {'form': form, 'student': student})
    
    form = comeval.objects.get(CE_id=id) 
    student = Student.objects.get(S_id=id)
    return render(request, 'scomform.html', {'student': student, 'form': form})


def Sprogresseval(request, id):
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
            PE_id=id, PEF=1)

        sub.save()
        Student.objects.filter(S_id=id).update(PE_S=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=1)
        endTermForm = Endterm.objects.filter(SE=id, SEF=1)
        Compform = comeval.objects.filter(CE_id=id)
        Progress = progresseval.objects.filter(PE_id=id, PEF=1)
        return render(request, 'Details.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm':
                                                 endTermForm, 'Compform': Compform, 'Progressform': Progress})

    Comp = progresseval.objects.filter(PE_id=id, PEF=1)
    if Comp.exists():
        form = progresseval.objects.get(PE_id=id, PEF=1)
        student = Student.objects.get(S_id=id)
        return render(request, 'progresseval.html', {'form': form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'progevaldet.html', {'student': student})


def Cprogresseval(request, id):
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
            PE_id=id, PEF=2)

        sub.save()
        Student.objects.filter(S_id=id).update(PE_C=True)
        detai = Student.objects.get(S_id=id)
        midTermForm = mideterm.objects.filter(SM=id, SF=2)
        endTermForm = Endterm.objects.filter(SE=id, SEF=2)
        Compform = comeval.objects.filter(CE_id=id)
        Progress = progresseval.objects.filter(PE_id=id, PEF=2)
        return render(request, 'cdetails.html', {'det': detai, 'midTermForm': midTermForm, 'endTermForm':
                                                 endTermForm, 'Compform': Compform, 'ProgressForm': Progress})

    Comp = progresseval.objects.filter(PE_id=id, PEF=2)
    if Comp.exists():
        form = progresseval.objects.get(PE_id=id, PEF=2)
        student = Student.objects.get(S_id=id)
        return render(request, 'cprogresseval.html', {'form': form, 'student': student})

    student = Student.objects.get(S_id=id)
    return render(request, 'cprogevaldet.html', {'student': student})


def Svpro(request,id):
    collegesu=CollegeSuper.objects.get(Co_id=id)
    return render(request,'collegesuper.html',{'collegesuper':collegesu})

def cvpro(request,id):
    comper=compper.objects.get(P_id=id)
    field_name = 'PC'
    field_object = compper._meta.get_field(field_name)
    field_value = field_object.value_from_object(comper)
    company_name = company.objects.get(C_id = field_value)
    return render(request,'companysuper.html',{'compper':comper , 'company' : company_name})
    
def fillInternFeedback(request,id):
    if request.method == 'POST':
       print(request.POST.get('mark1'))
       print(request.POST.get('mark2'))
       print(request.POST.get('mark3'))
       print(request.POST.get('mark4'))
       print(request.POST.get('mark5'))
       print(request.POST.get('mark6'))
       print(request.POST.get('mark7'))
       print(request.POST.get('mark8'))
       print(request.POST.get('mark9'))
       print(request.POST.get('mark10'))
       print(request.POST.get('mark11'))
       print(request.POST.get('mark12'))
       print(request.POST.get('mark13'))
       print(request.POST.get('mark14'))
       print(request.POST.get('mark15'))
       print(request.POST.get('mark16'))
       print(request.POST.get('mark17'))
       print(request.POST.get('mark18'))
       print(request.POST.get('mark19'))

       stu = Student.objects.get(S_id=id)
       return render(request, "studet.html", {'stu': stu})
        
    return render(request, 'internFeedbackFormDet.html' , {'id' : id})


def fillCompanyFeedback(request,id):
    if request.method == 'POST':
        pass
    return render(request, 'companyFeedbackFormDet.html' , {'id' : id})




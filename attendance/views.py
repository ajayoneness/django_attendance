from django.http import HttpResponse
from django.shortcuts import render
from students.models import students,teachers,presentabsent
from datetime import datetime,date
from uuid import uuid1
import pandas as pd
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os


data = pd.read_excel (r'C:\Users\codeAj\Desktop\Django Project\Attendance project\BackEnd\attendance\students\student.xlsx')
df = pd.DataFrame(data)

def index(request):
    teacher=teachers.objects.all()
    branch = ['computer Science','civil','mechinical','AI/DS','EC','Ex']
    sem=['1st','2nd','3rd','4th','5th','6th','7th','8th']

    return render(request,'index.html',{'teacher':teacher,'sem':sem,'branch':branch})


def student(request):
    stu = students.objects.all()
    try:
        bran = request.POST['branch']
        semester = request.POST['sem']
        teach = request.POST['teacher']
        sub = request.POST['subject']
        tim=datetime.now()
        request.session['branch'] = bran
        request.session['sem'] = semester
        request.session['teacher'] = teach
        request.session['subject'] = sub

        print(bran,semester,teach,sub)
        if bran == 'computer Science' and semester == '6th' and teach != '' and sub != '':
            return render(request, 'main.html',
                      {'cdate': tim, 'branch': bran, 'sem': semester, 'teacher': teach, 'sub': sub, 'stu': stu})
        else :
            return index(request)
    except:
        pass
    return index(request)


def submit(request):
    today = datetime.now()
    d3 = today.strftime("%Y-%m-%d %H:%M:%S")

    branch = request.session.get('branch')
    sem = request.session.get('sem')
    teacher = request.session.get('teacher')
    sub = request.session.get('subject')
    print(branch,sub,sem,teacher)

    studentList = request.POST.getlist('checkbox')
    #print(presentabsent.objects.all())
    i=0
    dic=dict()
    for enroll in studentList:
        stu = students.objects.get(enrollment_no=f'{enroll}')
        pa = presentabsent(request)
        pa.id = str(uuid1())
        pa.date = d3
        pa.enrollment = str(f'{enroll}')
        pa.sub = str(f'{sub}')
        pa.sem = str(f'{sem}')
        pa.teacher = str(f'{teacher}')
        pa.name = str(stu.name)
        key = enroll
        value = [str(i),pa.date,pa.enrollment,pa.sub,pa.sem,pa.teacher,pa.name,branch]

        dic.update({key:value})
        pa.save()
        print(dic)
        i = i + 1
    return render(request,'result.html',{'dic':dic,'teacher':pa.teacher,'date':pa.date,'subject':pa.sub})

def search(request):
    teacher = teachers.objects.all()
    print(teacher[2].subject)
    try:
        teacher = teachers.objects.all()
        enrl = request.POST['search']
        timdt = request.POST['start']
       # allpa=presentabsent.objects.all().distinct()
        palis=[]
        total=0
        for i in range(1,32):
            clis = []
            s=0
            clis.append(f'{timdt}-{str(i).zfill(2)}')
            for j in range(0,7):
                datecount = presentabsent.objects.filter(date__startswith=f'{timdt}-{str(i).zfill(2)}',enrollment=enrl,sub=teacher[j].subject).count()
                s=s+int(datecount)
                clis.append(datecount)
            clis.append(s)
            if clis[-1] != 0:
                total=total+clis[-1]
                palis.append(clis)
        print(total)


        #disti=presentabsent.objects.filter(date__startswith=timdt , enrollment=enrl).count()
        #print(disti)

        st = students.objects.get(enrollment_no = f"{enrl}")
        #pA=presentabsent.objects.filter(enrollment=f'{enrl}' , date__icontains=timdt)

        return render(request, 'stsearch.html', {"teacher": teacher,'cdate':datetime.now(),'name':st.name,'branch':st.branch,'palis':palis, 'tatt':total})

    except:
        pass
    return render(request,'stsearch.html',{"teacher":teacher})



def attendance(request):
    import os
    dt=datetime.now()
    cdt=dt.strftime('%Y-%m')

    headList= ['Name', 'Enrollment', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,'Total']
    try:
        #os.remove('demo.xlsx')
        teacher = teachers.objects.all()
        stu = students.objects.all()
        timdt = request.POST['start']
       # allpa=presentabsent.objects.all().distinct()
        palis=[]
        total=0
        for i in range(1,47):
            clis = []
            clis.append(f'{stu[i].name}')
            clis.append(f'{stu[i].enrollment_no}')
            s=0
            for j in range(1,32):
                datecount = presentabsent.objects.filter(date__startswith=f'{timdt}-{str(j).zfill(2)}',enrollment = str(stu[i].enrollment_no)).count()
                clis.append(datecount)
                s=s+int(datecount)
            clis.append(s)
            palis.append(clis)

#Excel file creation.........
        dic=dict()
        for j in range(0,34):
            lis=[]
            for i in palis:
                lis.append(i[j])
            value=lis
            key=str(headList[j])
            dic.update({key: value})

        df = pd.DataFrame(dic)
        writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()
        print('excel file created............')

        return render(request, 'monthsearch.html', {'headtable':headList,"teacher": teacher,'cdate':datetime.now(),'palis':palis, 'tatt':total,'cdt':cdt})

    except:
        pass
    return render(request,'monthsearch.html',{'headtable':headList,'cdt':cdt})



def download(request):
    try:
        #filepath=os.path.join(os.path.dirname(os.path.dirname(__file__)),'demo.xlsx')
        #filename = 'test.txt'
        #filepath = base_dir + '\\Files\\' + filename
        #thefile = filepath
        #filename = os.path.basename(thefile)
        #chunk_size = 8192
        #response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type=mimetypes.guess_type(thefile)[0])
        #response['Content-Length'] = os.path.getsize(thefile)
        #response['Content-Disposition'] = "Attachment;filename=%s" % filename
        #return request
        return HttpResponse('Download Completed !!')
    except:
        return HttpResponse('Download Completed !!')

def contact(request):
    return render (request,'contactUs.html')
from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *
from app1.models import *

def sC(request):
    SIO=SchoolInfoUI()
    if request.method=='POST':
        sss=SchoolInfoUI(request.POST)
        if sss.is_valid():
            s1=sss.cleaned_data['schname']#retriving values based on paticular  key in this dictionary
            s2=sss.cleaned_data['schlocation']
            s3=sss.cleaned_data['schsubjects']
            SCO=SchoolInfo.objects.get_or_create(scname=s1,sclocation=s2,subjects=s3)
            return HttpResponse('Successfully created in SchoolInfo Table')
        else:
            return HttpResponse('invaild given input data')
        
    dd={'SIO':SIO} 
    return render(request,'h1.html',dd)



def sCC(request):
    SIO=SchoolInfoUII()
    if request.method=='POST':
        sss=SchoolInfoUII(request.POST)
        if sss.is_valid():
            sss.save()
            return HttpResponse('Successfully created in SchoolInfo Table')
        else:
            return HttpResponse('invaild given input data')
    
    dd={'SIO':SIO} 
    return render(request,'h1.html',dd)







def sT(request):
    STIO=StudentInfoUI()
    if request.method=='POST':
        ttt=StudentInfoUI(request.POST)#collect the data 
        if ttt.is_valid():#validate the data 
            t1=ttt.cleaned_data['schsubjects']#based on the parent primary key column data i need to insert the data in the child column
            t2=ttt.cleaned_data['sttname']
            t3=ttt.cleaned_data['sttgender']
            t4=ttt.cleaned_data['sttage']
            t5=ttt.cleaned_data['sttlocation']
            SCO=StudentInfo.objects.get_or_create(subjects=t1,stname=t2,gender=t3,age=t4,stlocation=t5)
            return HttpResponse('Successfully created in StudentInfo Table')
        else:
            return HttpResponse('invaild given input data')
    dd={'STIO':STIO} 
    return render(request,'h2.html',dd)



def sTT(request):
    STIO=StudentInfoUII()
    if request.method=='POST':
        sss=StudentInfoUII(request.POST)
        if sss.is_valid():
            sss.save()
            return HttpResponse('Successfully created in StudentInfo Table')
        else:
            return HttpResponse('invaild given input data')
    
    dd={'STIO':STIO} 
    return render(request,'h2.html',dd)


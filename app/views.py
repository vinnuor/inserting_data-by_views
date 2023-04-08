from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *


def insert_dept(request):
    deptnum=input('enter deptnumber  :')
    dname=input('enter dname :')
    loc=input('enter location  :')
    DO=Dept.objects.get_or_create(deptno=deptnum,dname=dname,loc=loc)[0]
    DO.save()
    return HttpResponse('dept table is inserted')

def insert_emp(request):
    deptnum=input('enter deptnum  :')
    empno=input('enter emp number  :')
    ename=input('enter ename  :')
    
    DO=Dept.objects.get_or_create(deptno=deptnum)[0]
    DO.save()
    EO=Emp.objects.get_or_create(deptno=DO,empno=empno,ename=ename)[0]
    EO.save()
    return HttpResponse('employe data is inserted ')


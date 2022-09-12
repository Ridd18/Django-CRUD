import re
from django.shortcuts import render
from .models import *
from django.contrib import messages
from .forms import StudentForm



def studentDisplay(request):
    results = EventRegister.objects.all()
    return render(request,"index.html",{"EventRegister":results}) 

def studentEdit(request,id):
    getStudentDetailsByStudentID = EventRegister.objects.get(id=id)
    return render(request,"edit.html",{"EventRegister":getStudentDetailsByStudentID}) 

def studentUpdate(request,id):
    getStudentDetailsForUpdate= EventRegister.objects.get(id=id)
    form = StudentForm(request.POST,instance=getStudentDetailsForUpdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The student record is updated succesfully")
        return render(request,"edit.html",{"EventRegister":getStudentDetailsForUpdate})

def studentDelete(request,id):
    deleteStudent = EventRegister.objects.get(id=id)
    deleteStudent.delete()
    results = EventRegister.objects.all()
    messages.success(request,"The student record is deleted succesfully")
    return render(request,"index.html",{"EventRegister":results}) 

def studentRegister(request):
    if request.method == 'POST':
        if request.POST.get('Rollno') and request.POST.get('Name') and request.POST.get('Class') and request.POST.get('Age'):
            saveStudent = EventRegister()
            saveStudent.Rollno = request.POST.get('Rollno')
            saveStudent.Name = request.POST.get('Name')
            saveStudent.Class = request.POST.get('Class')
            saveStudent.Age = request.POST.get('Age')
            saveStudent.save() 
            messages.success(request,"The record"+ saveStudent.Name +"is saved successfully")
            return render(request,"create.html") 
        else:
            return render(request,"create.html") 
    else:
        return render(request,"create.html") 


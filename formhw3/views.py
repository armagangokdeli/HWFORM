from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import RequestContext
from formhw3.forms import *
from formhw3.models import *


def addteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        office_details=form.cleaned_data["office_details"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"],)
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = TeacherForm()
    return render_to_response('addteacher.html', {'form': form},RequestContext(request))

def all_teachers(request):
    return render_to_response('all_teachers.html', {'teacher_list': Teacher.objects.all()})


def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"],)
            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = StudentForm()
    return render_to_response('addstudent.html', {'form': form},RequestContext(request))

def all_student(request):
    return render_to_response('all_students.html', {'student_list': Student.objects.all()})

def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Course(name=form.cleaned_data["name"],
                        code=form.cleaned_data["code"],
                        classroom=form.cleaned_data["classroom"],
                        times=form.cleaned_data["times"],)
            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = CourseForm()
    return render_to_response('addcourse.html', {'form': form},RequestContext(request))

def all_course(request):
    return render_to_response('all_courses.html', {'course_list': Course.objects.all()})
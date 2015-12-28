from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

class TeacherForm(forms.Form):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    office_details = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField()


class CourseForm(forms.Form):

    name = forms.CharField(max_length=100)
    code = forms.CharField(max_length=100)
    classroom = forms.CharField(max_length=100)
    times = forms.CharField(max_length=100)
''' students = forms.ManyToManyField(Student)
    teacher = forms.ForeignKey(Teacher)'''

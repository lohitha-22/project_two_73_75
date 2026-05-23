from django.shortcuts import render,redirect,get_object_or_404
from app1.models import student
from app1.forms import student_form

from app1.forms import student_delete_form

from django.http import HttpResponse

'create & read'
'------------'


def student_list(request):
    data = student.objects.all()
    form = student_form()

    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    return render(request,'student_list.html',{'data':data,'form':form})


'update'
'-------'



def student_update(request,id):
    std = get_object_or_404(student, id=id)
    form = student_form(instance=student)

    if request.method == 'POST':
        form = student_form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    return render(request, 'student_update.html',{'form':form})



'delete'
'------'

def delete_student(request,id):
    def_username = 'lohi'
    def_password = 'lohi123'
    std = student.objects.get(id = id)

    del_form = student_delete_form()

    if request.method == 'POST':
        del_form = student_delete_form(request.POST)
        if del_form.is_valid():
            user = del_form.cleaned_data['username']
            password = del_form.cleaned_data['password']

            if user == def_username and password == def_password:
                std.delete()

                return redirect('home_page')
            else:
                return HttpResponse('<h1>invalid username/password</h1>')

    return render(request,'delete_std.html',{'del_form':del_form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import person
from .forms import personform
from django.db.models import Q 

#หน้าบ้าน
def home(request):
    application = person.objects.all()
    return render(request,'index.html',{'applications': application})

#รับข้อมูลพนักงาน
def add_application(request):
    if request.method == 'POST':
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = personform()
    return render(request,'form.html',{'form':form}) 

#แก้ไขข้อมูลพนักงาน
def edit_application(request, pk):
    application = get_object_or_404(person,pk=pk)
    if request.method == 'POST':
        form = personform(request.POST, instance=application)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else :
        form = personform(instance=application)
    return render(request,'edit.html',{'form':form,'application':application})

#ลบข้อมูลพนักงาน
def delete_application(request, pk):  
    application = get_object_or_404(person, pk=pk)
    application.delete()
    return redirect('home')

#ค้นหาข้อมูลพนักงาน
def search_application(request):
    query = request.GET.get('q','')
    application = person.objects.filter(
        Q(first_name__icontains=query)|
        Q(last_name__icontains=query)|
        Q(position_applied__icontains=query) 
    )
    return render(request,'search.html',{'application':application,'query':query})


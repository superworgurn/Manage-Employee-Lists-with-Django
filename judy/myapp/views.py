# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import person
from .forms import personform, EditForm
from django.db.models import Q

def home(request):
    application = person.objects.all()
    return render(request, 'index.html', {'applications': application})

def add_application(request):
    if request.method == 'POST':
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = personform()
    return render(request, 'form.html', {'form': form})

def edit_application(request, pk):
    application = get_object_or_404(person, pk=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditForm(instance=application)
    return render(request, 'edit.html', {'form': form, 'application': application})

def delete_application(request, pk):
    application = get_object_or_404(person, pk=pk)
    application.delete()
    return redirect('home')

def search_application(request):
    query = request.GET.get('q', '')
    application = person.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(position_applied__icontains=query)
    )
    return render(request, 'search.html', {'application': application, 'query': query})

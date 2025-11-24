from django.shortcuts import render, redirect
from .forms import TeenagerApplicationForm

def teenager_application(request):
    if request.method == 'POST':
        form = TeenagerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TeenagerApplicationForm()
    return render(request, 'teenager_form.html', {'form': form})

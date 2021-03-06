from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created !You can redirect now ')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'account/register.html', {'form':form})
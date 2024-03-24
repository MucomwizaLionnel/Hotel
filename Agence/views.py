from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from Agence.form import UserForm

# Create your views here.
def home(request):
    error=''
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            if user.is_gerant:
                return redirect('gerant')
            elif user.is_caissiere:
                return redirect('caissiere')
            else:
                return redirect('touriste')
        else:
            error='Le username ou mots de pass est incorrect'
    return render(request,'login.html',{'error':error})

def register(request):
    form=UserForm()

    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'register.html',{'form':form})

def gerant(request):
    return render(request,'gerant.html')
def caissiere(request):
    return render(request,'caissiere.html')
def touriste(request):
    return render(request,'touriste.html')

      




def login(request):
    return render(request,'login.html')

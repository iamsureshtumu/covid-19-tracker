from django.shortcuts import redirect #"go to the post_detail page for the newly created post"

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from app import forms
from django.contrib.auth.decorators import login_required

from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
@login_required    
def homepage(request):
    # ctg1=Sslc.objects.all()
    user_name=request.session.get('username',"No User") 
    context = {
        'user_name':user_name
    }
    return render(request,'homepage.html',context)


def register(request):
    register=False
    if request.method=="POST":
        user_form=forms.User_Form(request.POST)
        user_data_form=forms.User_data_form(request.POST,request.FILES)
        if user_form.is_valid() and user_data_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            user_data=user_data_form.save(commit=False)
            user_data.user=user

            if 'profile_pic' in request.FILES:
                user_data.profile_pic=request.FILES['profile_pic']
            user_data.save()
            register=True
            send_mail("Registration Successful","Thank You For Registering","noreply2user.infotech@gmail.com", \
                [user.email],fail_silently=True) 
     #here we give user.email.............so it will also send to the unknow person who is going to signup here
    else:
        user_form=forms.User_Form()
        user_data_form=forms.User_data_form()
    
    d={'form':user_data_form,'form_user':user_form,'register':register}
    return render(request,'app/register.html',context=d)

def index(request):
    user_name=request.session.get('username',"No User")
    return render(request,'app/base.html',context={'user_name':user_name})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username',"")
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # request.session['username']=username
                request.session['username']=(username) #,user.email
# here we want to display both username&profile_pic after login...username & email are working
# profilepic need to check and need to give the path
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("Not an Active user")
        else:
            print("Invalid Login")
            return render(request,'app/login.html')
            # return HttpResponse("Invalid Login")
    else:
        return render(request,'app/login.html')
        # return render(request,'homepage.html')


@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('index'))
    

@login_required
def wish(request):
    # return HttpResponse("<h1>Hai Mr./Ms. {} </h1>".format(request.session['username']))
    return HttpResponse("<h1>Hai Mr./Ms. {} </h1>")

from django.shortcuts import  render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.contrib import messages
from users.models import User

APPLICATION = "authentification/landing"
class SigninView(View):
    view_name = "signin"
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request,self.template)
    
    def post(self,request, *args, **kwargs):

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('home')
        messages.warning(request,'username or password not valid')    
        return redirect('signin')


def logoutHome(request):
    logout(request)
    return redirect('signin')            

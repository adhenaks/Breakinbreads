from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView
from bakery.forms import RegisterationForm,LoginForm,CategoryCreateForm
from bakery.models import User,Category
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


class SignUpView(CreateView):

    template_name="bakery/register.html"
    form_class=RegisterationForm
    model=User
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,"failed to create account")
        return super().form_invalid(form)

class SignInView(FormView):
    template_name="bakery/login.html"
    form_class=LoginForm

    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("signin")   
            else:
                messages.success(request,"invalid creadential")
                return render(request,self.template_name,{"form":form})

class CategoryCreateView(CreateView,ListView):
    template_name="bakery/category_add.html"
    form_class=CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("add-category")

    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)
                             
                             
                             
                             
        








from django.shortcuts import render , redirect ,HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout  
from django.contrib.auth.decorators import login_required
import random

def ind(request) :
    obj = foods.objects.all()
    ads = profile.objects.all( )
    if request.user.is_authenticated :
        ud = profile.objects.get(usern=request.user)
        if request.method == 'POST' :
            name = request.POST.get('n')
            email = request.POST.get('e')
            des = request.POST.get('de')
            cont = contact(username=request.user,name=name, email=email,desc=des)
            cont.save()
            return redirect('main')
    else :
        ud = 'NONE'
     
    return render(request,'index.html' ,{'obj':obj ,'ad':ud})

def signed(request) :
    form = UserCreationForm()
    if request.method == 'POST' :
        nf = UserCreationForm(request.POST)
        if nf.is_valid() :
            nf.save()
            user = nf.cleaned_data.get('username')
            po = User.objects.get(username=user)
            p = profile(usern =po)
            p.save()
            return redirect('main')
        else :
            return HttpResponse("your inputed data must be in wrong format either its your password or username....")
        
        
    return render(request , 'sign.html' , {'form':form})

def loginic(request) :
    if request.method == 'POST' :
        us = request.POST.get('u')
        pas = request.POST.get('p')
        ok = authenticate(username=us , password=pas)
        if ok is not None :
            login(request,ok)
            return redirect('main')
        else :
            return HttpResponse("your inputed data is wrong pls enter it correctly...")
    return render(request , 'logini.html')

def getout(request) :
    logout(request)
    return redirect('main')
@login_required(login_url='lo')
def cart(request ,pk) :
    ud = profile.objects.get(usern=request.user)
    p = ud.item.all()
    li = 0
    for i in p :
        li += int(i.price)  

    if request.method == 'POST' :
        product = foods.objects.get(id=pk)
        ud.item.add(product)
        return redirect('cart' , pk=ud.id)
    return render(request , 'cart.html' ,{'p':p ,'x':li})
def remo(request,pk) :
    ud = profile.objects.get(usern=request.user)
    p = ud.item.all()
    if request.method == 'POST' :
        product = foods.objects.get(id=pk)
        ud.item.remove(product)
        return redirect('cart' , pk=ud.id)
    return render(request ,'cart.html',{'p':p})
def pay(request,pk) :
    ud = profile.objects.get(usern=request.user)
    p = ud.item.all()
    a = int(pk)
    gs = a*18/100
    dc = 50
    pc = 5
    total = a+gs+dc+pc
    context = {'ab':total,'gs':gs ,'dc':dc,'pc':pc,'a':a ,'p':p}
    return render(request ,'pay.html' , context)
def offer(request,pk) :
    ud = profile.objects.get(usern=request.user)
    p = ud.item.all()
    a = float(pk)
    gs = a*18/100
    of = random.randint(100,120)
    dc = 50
    pc = 5
    total = a-of
    cont = {'a':a ,'gs':gs ,'dc':dc,'pc':pc,'total':total,'p':p , 'of':of}
    return render(request ,'offerpage.html' , cont)


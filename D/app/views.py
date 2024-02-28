from django.shortcuts import render, redirect
from django import forms

from .models import DB
# Create your views here.

class DBF(forms.ModelForm):
    class Meta:
        model = DB
        fields = '__all__'

def home(req):
    f = DBF()
    if req.method == 'POST':
        f = DBF(req.POST)
        if f.is_valid():
            f.save()
            return redirect('/')
    
    return render(req, 'home.html',{'f':f, 'db':DB.objects.all()})

def up(req, id):
    db = DB.objects.get(pk=id)
    f = DBF(instance=db)
    if req.method == 'POST':
        f = DBF(req.POST, instance=db)
        if f.is_valid():
            f.save()
            return redirect('/')
    
    return render(req, 'up.html',{'f':f, 'db':db})
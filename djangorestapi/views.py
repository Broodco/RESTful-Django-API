from django.shortcuts import render, redirect
from django.http import HttpResponse

def redirectapi(request):
    return redirect('/api')
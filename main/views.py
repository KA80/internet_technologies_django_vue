from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, Template


def index(request):
    return render(request, 'main/index.html')

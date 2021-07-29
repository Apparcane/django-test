from django import template
from django import http
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# def index(request):
#     template = loader.get_template('index.html')
#     context = {}
#     render_page = template.render(context, request)
#     return HttpResponse(render_page)

# def index(request):
#     return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')

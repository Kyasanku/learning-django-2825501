from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>Home View</p>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p>Pet detail view with id {pet_id}</p>')
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json

# Create your views here.

def health_check(request):
    return HttpResponse('All clear! Server is running. :)', status=200)

# REPLACE CSRF_EXEMPT WITH A MORE SECURE ANNOTATION
@csrf_exempt
def save_url(request):
    if request.method != 'POST':
        return HttpResponse('Bad request', status=400)
    
    body = json.loads(request.body)

    url = body['url']

    return HttpResponse(url, status=200)

@csrf_exempt
def get_url(request, code):
    return HttpResponse(code, status=200)
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *

import json, random

# Create your views here.

BASE_URL = "http://127.0.0.1:8000/url/"

# Helper method
# Used to generate unique code
def generate_code():
    code = ""
    allowlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~-_."
    for _ in range(10):
        chosen_ascii_code = random.choice(allowlist)
        code += chosen_ascii_code
    return code

def health_check(request):
    return HttpResponse(f'All clear! Server is running. :)', status=200)

# REPLACE CSRF_EXEMPT WITH A MORE SECURE ANNOTATION
@csrf_exempt
def save_url(request):
    if request.method != 'POST':
        return HttpResponse('Bad request', status=400)
    
    body = json.loads(request.body)

    url = body['url']

    encoding = generate_code()

    Link.objects.create(code=encoding, url=url)

    result = BASE_URL + encoding

    return HttpResponse(f'URL saved: {result}', status=200)

def get_url(request, code):
    try:
        link_object = Link.objects.get(pk=code)
    except Link.DoesNotExist as e:
        return HttpResponse('Code not found in DB', status=400)
    except Exception as e:
        return HttpResponse('Something went wrong in the server. Please try again.', status=500)
    return HttpResponse(f"{getattr(link_object, 'url')}", status=200)

def get_and_redirect_url(request, code):
    try:
        link_object = Link.objects.get(pk=code)
    except Link.DoesNotExist as e:
        return HttpResponse('Code not found in DB', status=400)
    except Exception as e:
        return HttpResponse('Something went wrong in the server. Please try again.', status=500)
    return redirect(f"{getattr(link_object, 'url')}")
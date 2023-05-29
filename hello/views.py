import re
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.utils.timezone import datetime
from django.http import HttpResponse

import requests
from django.http import JsonResponse


def get_my_ip(request):
    res = requests.get("http://ip.jsontest.com/")
    x = {'foo':'bar'}
    return JsonResponse(res.json())

def home(request):
    return HttpResponse("Hello, Django!")

#def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import base64
import logging
import logging.config
from logging import handlers

def login(request):
    print("login")
     # if request.is_ajax():
     #
     #    inputId = request.POST.get('inputId')
     #    inputPw = request.POST.get('inputPw')
    logging.debug('login 페이지 접속')
    return render(request, 'login/login.html')
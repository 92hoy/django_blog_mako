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
from backend.models import User

def login(request):
    print("login")
     # if request.is_ajax():
     #
     #    inputId = request.POST.get('inputId')
     #    inputPw = request.POST.get('inputPw')
    logging.debug('login 페이지 접속')

    # ------login session example-------
    # inputId = request.POST.get('inputId')
    # inputPw = request.POST.get('inputPw')
    #
    # if userObject.user_pwd == inputPw:
    #             request.session['user_id'] = userObject.user_id
    #             request.session['user_name'] = userObject.user_name
    #             request.session['language'] = userObject.language
    #             request.session['user_role'] = userObject.user_role
    #             request.session[translation.LANGUAGE_SESSION_KEY] = userObject.language
    #             translation.activate(userObject.language)
    #
    #             return JsonResponse({'result':'success'})
    # ------login session example-------
    return render(request, 'login/login.html')

def regist(request):

    #Post.objects.create(user_id=me, password='Sample title', name='Test',ph='')

    logging.debug('계정생성 Test')

    return JsonResponse({'return':'success'})
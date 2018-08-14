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

    if request.is_ajax():

        inputId = request.POST.get('inputId')
        inputPw = request.POST.get('inputPw')

        with connections['default'].cursor() as cur:
            query = '''
                      select user_id,user_pw
                      FROM User
                      where user_id = '{user_id}' and user_pw='{user_pw}'
                '''.format(user_id=inputId,user_pw=inputPw)
            cur.execute(query)
            rows = cur.fetchall()
            print(rows)

            if len(rows) !='0':
                with connections['default'].cursor() as cur:
                    query = '''
                              select user_id,name,user_role
                              FROM User
                              where user_id = '{user_id}'
                        '''.format(user_id=inputId,user_pw=inputPw)
                    cur.execute(query)
                    row = cur.fetchall()
                request.session['user_id'] = row[0]
                request.session['user_name'] = row[1]
                request.session['user_role'] = row[2]

                logging.debug(inputId,'(',name,')','login 페이지 접속')
                return JsonResponse({'return':'success'})
            else :
                logging.warning('ID',inputId,'PW',inputPw,'login 실패')
                return JsonResponse({'return':'false'})



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
    if request.is_ajax():
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        name = request.POST.get('user_name')
        ph = request.POST.get('ph')

        with connections['default'].cursor() as cur:
            query = '''
                      INSERT INTO main.User
                                  (user_id,
                                  password,
                                  name,
                                  ph
                                  )
                      VALUES ('{user_id}',
                              '{user_pw}',
                              '{name}',
                              '{ph}')
                '''.format(user_id=user_id,user_pw=user_pw,name=name,ph=ph)
            cur.execute(query)
    #User.objects.create(user_id=user_id, password=user_pw, name=name,ph=ph)

    logging.debug('계정생성 Test')

    return JsonResponse({'return':'success'})
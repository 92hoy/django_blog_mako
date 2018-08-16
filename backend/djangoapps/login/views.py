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
    print("login!")

    if request.is_ajax():

        inputId = request.POST.get('user_id')
        inputPw = request.POST.get('password')
        print(inputId,inputPw)
        with connections['default'].cursor() as cur:
            query = '''
                      select user_id,password
                      FROM User
                      where user_id = '{user_id}' and password='{password}'
                '''.format(user_id=inputId,password=inputPw)
            cur.execute(query)
            rows = cur.fetchall()
            l_rows = len(rows)


        if l_rows != 0:

            with connections['default'].cursor() as cur:
                query = '''
                          select user_id,name,user_role
                          FROM User
                          where user_id = '{user_id}'
                    '''.format(user_id=inputId)
                cur.execute(query)
                row = cur.fetchall()

                print(row,'rows list=',row[0][0],row[0][1],row[0][2])

                request.session['user_id'] = row[0][0]
                request.session['user_name'] = row[0][1]
                request.session['user_role'] = row[0][2]

                logging.debug('login 페이지 접속')
            return JsonResponse({'return':'success'})
        else :
            logging.warning('ID=',inputId,'PW=',inputPw,'login 실패')
            return JsonResponse({'return':'false'})

        #login_out에 쓸거
        # try:
        #     del request.session['member_id']
        # except KeyError:
        #     pass

    return render(request, 'login/login.html')

def regist(request):

    print("regist")

    if request.is_ajax():
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('password')
        name = request.POST.get('name')
        ph = request.POST.get('ph')

        with connections['default'].cursor() as cur:
            query = '''
                      INSERT INTO User
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
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
from backend.models import Board

def board(request):
    print("board")
     # if request.is_ajax():
     #
     #    inputId = request.POST.get('inputId')
     #    inputPw = request.POST.get('inputPw')
    logging.debug('=======login========debug')
    logging.debug('login 페이지 접속')

    logging.debug('========login=======debug')
    return render(request, 'board/board.html')
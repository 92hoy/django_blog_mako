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


def about(request):
    print("about_chart")
    # if request.is_ajax():
    #
    #    inputId = request.POST.get('inputId')
    #    inputPw = request.POST.get('inputPw')
    #logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
    logging.debug('===============debug')
    logging.debug('About 페이지 접속')
    logging.info('info 페이지 접속')
    logging.warn('warn')
    logging.error('error 페이지 접속')
    logging.critical('critical 페이지 접속')
    logging.debug('===============debug')
    # mylogger = logging.getLogger()
    # mylogger.setLevel(logging.INFO)
    #
    # rotatingHandler = logging.handlers.TimedRotatingFileHandler(filename='example.log', when='M', interval=1, encoding='utf-8')
    #
    # fomatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    #
    # rotatingHandler.setFormatter(fomatter)
    # mylogger.addHandler(rotatingHandler)
    #
    #
    # logging.config.fileConfig('logging.conf')
    #
    # # create logger
    # logger = logging.getLogger('simpleExample')
    #
    # # 'application' code
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warn('warn message')
    # logger.error('error message')
    # logger.critical('critical message')

    return render(request, 'about/about.html')


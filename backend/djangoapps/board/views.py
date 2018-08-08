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

    logging.debug('게시판 페이지 접속')

    b_data = Board.objects.all()
    print("data all = ",b_data)
    return render(request, 'board/board.html')

def board_add(request):


    if request.is_ajax():

        title = request.POST.get('title_input')
        content = request.POST.get('content_input')
        me = User.objects.get(username='JHY')

        board_add = Board(user_id=me, title=title, content=content)
        board_add.save()

        print(title)
        print(content)
        logging.debug('게시글 작성')


    JsonResponse({'return':'success'})
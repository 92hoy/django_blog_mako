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

    try:
        request.session['user_id']
    except KeyError:
        return render(request, 'login/login.html')

    logging.debug('게시판 페이지 접속')

    board_data = Board.objects.all()

    for data in board_data:
        id = data.user_id
        title = data.title
        content = data.content
        print(id,'/',title,'/',content)


    board_list=list()
    for b_data in board_data:
        data_dict =dict()
        data_dict['board_seq'] = b_data.board_seq
        data_dict['user_id'] = b_data.user_id
        data_dict['title'] = b_data.title
        data_dict['content'] = b_data.content
        data_dict['create_date'] = b_data.create_date
        board_list.append(data_dict)

    print(board_list)
    context = {'board_list': board_list}
    print("data all = ",board_data)
    return render(request, 'board/board.html',context)

def board_add(request):


    if request.is_ajax():

        title = request.POST.get('title_input')
        content = request.POST.get('content_input')
        user = request.session['user_id']
        print (user)

        if len(user) ==0:
            return({"return":"fail"})
        else:

            Board.objects.create(user_id=user, title=title, content=content)



        logging.debug('게시글 작성')


    return JsonResponse({'return':'success'})

def board_del(request):

    seq = request.POST.get('seq')
    fb = Board.objects.get(board_seq=seq)
    fb.delete()
    return JsonResponse({"return":"success","seq":seq})
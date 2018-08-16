# django default
from django.urls import path
from django.conf.urls import url

#login / logout
from .djangoapps.login import views as LoginViews
from .djangoapps.board import views as BoardViews
from .djangoapps.logout import views as LogoutViews
from .djangoapps.about import views as AboutViews

from .djangoapps.main import views as MainViews

urlpatterns = [
    url('login$', LoginViews.login, name='login'),
    url('logout$', LoginViews.logout, name='logout'),
    url('regist$', LoginViews.regist, name='regist'),
    url('about$', AboutViews.about, name='about'),

    #/backend/templates/board/board.html
    url('board$', BoardViews.board, name='board'),
    url('board_add$', BoardViews.board_add, name='board_add'),

    url('$', MainViews.main, name='main'),
]
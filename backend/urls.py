# django default
from django.urls import path
from django.conf.urls import url

#login / logout
from .djangoapps.login import views as LoginViews
from .djangoapps.logout import views as LogoutViews

from .djangoapps.main import views as MainViews

urlpatterns = [
    url('login$', LoginViews.login, name='login'),
    url('$', MainViews.main, name='main'),
]
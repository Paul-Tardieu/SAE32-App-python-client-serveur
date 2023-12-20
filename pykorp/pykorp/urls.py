"""
URL configuration for pykorp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    #page home du site:
    path('pykorp', pykorp_render),

    #page de suivi des colis:
    path('pykorp/suivi', suivi_render),

    #page des expéditeurs:
    path('pykorp/expediteur', expediteur_render),

    #page des transporteurs:
    path('pykorp//transporteur', transporteur_render),

    #page d'admin:
    path('pykorp/admin', admin_render),

    #url dynamique:
    #re_path(r'^pykorp/(?P<ID>\w+)/$', ),
]

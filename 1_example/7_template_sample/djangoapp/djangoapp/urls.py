"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from myapp import views_template
from myapp import views_tvariable
from myapp import views_ttagsif
from myapp import views_ttagsfor
from myapp import views_ttagscomment
from myapp import views_ttagsblock
from myapp import views_ttable
from myapp import views_ttagsextends
from myapp import views_ttagsinclude

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/', views_template.index),
    
    path('tvariable/', views_tvariable.index),
    path('ttagsif/', views_ttagsif.index),
    path('ttagsfor/', views_ttagsfor.index),
    path('ttagscomment/', views_ttagscomment.index),
    path('ttable/', views_ttable.index),
    path('ttagsblock/', views_ttagsblock.index),
    path('ttagsextends/', views_ttagsextends.index),
    path('ttagsinclude/', views_ttagsinclude.index)
]
"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from app1.views import classes
from app1.views import students
from app1.views import spider
from app1.views import downLoad
urlpatterns = [
    #url(r'',classes.get_classes),#首页默认页面
    url(r'^admin/', admin.site.urls),
    url(r'^classes/get_classes.html$',classes.get_classes),
    url(r'^classes/add_classes.html$',classes.add_classes),
    url(r'^classes/del_classes.html$',classes.del_classes),
    url(r'^classes/edit_classes.html$',classes.edit_classes),
    url(r'^classes/',classes.get_classes),#首页默认页面

    url(r'^students/get_students.html$', students.get_students),
    url(r'^students/add_students.html$', students.add_students),
    url(r'^students/del_syudents.html$', students.del_students),
    url(r'^students/edit_students.html$', students.edit_students),
    url(r'^students/',students.get_students),#首页默认页面

    url(r'^spider',spider.f),
    url(r'^app_spider',spider.f),

    url(r'^download',downLoad.file_download),
]


"""
URL configuration for emp_management project.

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
# to add media
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),

    path('addemp',views.addemp,name="addemp"),
    path('delete/<int:eid>',views.emp_dlt,name="emp_dlt"),
    path('update/<int:eid>',views.emp_updt,name="emp_updt"),
    path('view/<int:eid>',views.emp_view,name="emp_view"),
    path('search',views.search_data,name="search"),

    path('search_male',views.search_male,name="search_male"),
    path('search_female',views.search_female,name="search_female"),

    path('asc_salary',views.asc_salary,name="asc_salary"),
    path('desc_salary',views.desc_salary,name="desc_salary"),


    path('search_dpt',views.search_dpt,name="search_dpt"),


    # path('view/update/<int:eid>',views.emp_updt,name="emp_updt"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

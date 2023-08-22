"""
URL configuration for vesb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('bdua.urls'))
# ]


# from django.contrib import admin
# from django.urls import path, include
# from bdua.api import PersonList, PersonDetail


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/person/', PersonList.as_view(), name='person-list'),
#     path('api/v1/person/<str:document_type>/<str:identification_number>/', PersonDetail.as_view(), name='person-detail'),
#     path('', include('bdua.urls')),  # Ajusta esto según el nombre real de la aplicación y su URLconf
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('person/', include('bdua.urls')),  # Ruta para la página de persona
    path('', include('bdua.urls')),  # Ruta para la URL raíz '/'
]






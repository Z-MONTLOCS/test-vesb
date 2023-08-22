# from django.urls import path
# from .api import PersonList, PersonDetail

# urlpatterns = [
#     path('api/v1/person/', PersonList.as_view(), name='person-list'),
#     path('api/v1/person/<str:document_type>/<str:identification_number>/', PersonDetail.as_view(), name='person-detail'),
# ]


from django.urls import path
from . import views
from .api import PersonList, PersonDetail








urlpatterns = [
    path('', PersonList.as_view(), name='person-list'),
    path('api/v1/person/', PersonList.as_view(), name='person-list'),
    path('api/v1/person/<str:document_type>/<str:identification_number>/', PersonDetail.as_view(), name='person-detail'),
]

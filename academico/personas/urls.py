from django.urls import path
from .views import *

urlpatterns = [
    path('v1/tdoc/', tipoDocumento_APIView.as_view()),
    path('v1/persona/', persona_APIView.as_view()),
]

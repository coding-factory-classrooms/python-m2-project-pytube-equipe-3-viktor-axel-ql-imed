# Create your views here.


from django.http import JsonResponse
from django.contrib.auth.models import User, Group


def home(request):
    return JsonResponse({
        "message": "Welcolme to Pytube API",
        "success": "true"
    })

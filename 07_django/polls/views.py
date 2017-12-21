from django.http import HttpResponse
from django.conf import settings

def index(request):
    return HttpResponse("SPECIAL_TEXT: " + settings.SPECIAL_TEXT)
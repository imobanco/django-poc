from django.http import HttpResponse
from time import sleep
from random import randint

def index(request):
    sleep_time = randint(0, 3)
    sleep(sleep_time)
    return HttpResponse(f"I sleept for {sleep_time}")
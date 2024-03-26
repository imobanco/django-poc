from django.http import HttpResponse
from time import sleep
from random import randint
from asyncio import sleep as asleep


def sync_sleep(request):
    sleep_time = randint(0, 3)
    sleep(sleep_time)
    return HttpResponse(f"I sleept for {sleep_time}")


async def async_sleep(request):
    sleep_time = randint(0, 3)
    await asleep(sleep_time)
    return HttpResponse(f"I sleept for {sleep_time}")


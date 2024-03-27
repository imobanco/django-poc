from typing import Any
from django.http import HttpRequest, HttpResponse
from time import sleep
from random import uniform
from asyncio import sleep as asleep
from .session import Session
from django.views import View
from asgiref.sync import async_to_sync, sync_to_async

class AsyncView(View):
    session: Session

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.session = Session()

    @async_to_sync()
    async def get(self, request, *args, **kwargs):
        user_email = request.GET.get('email')
        user_email = f"{user_email}@django-poc.com"
        print(f"email {user_email}")
        self.session.set_email(user_email)
        io_time = float(request.GET.get('sleep', 3.9))
        sleep_time = uniform(0, io_time)
        await asleep(sleep_time)
        return HttpResponse(f"I napped for {sleep_time} seconds - user {self.session.get_email()}")

def sync_sleep(request):
    user_email = request.GET.get('email')
    user_email = f"{user_email}@django-poc.com"
    io_time = float(request.GET.get('sleep', 3.9))
    sleep_time = uniform(0, io_time)
    sleep(sleep_time)
    return HttpResponse(f"I napped for {sleep_time} seconds")

async def async_sleep(request: HttpRequest):
    session = Session()
    user_email = request.GET.get('email')
    user_email = f"{user_email}@django-poc.com"
    print(f"email {user_email}")
    session.set_email(user_email)
    io_time = float(request.GET.get('sleep', 3.9))
    sleep_time = uniform(0, io_time)
    await asleep(sleep_time)
    print(f"This is my session {session}")
    return HttpResponse(f"I napped for {sleep_time} seconds - user {session.get_email()}")


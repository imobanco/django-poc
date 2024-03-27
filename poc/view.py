from django.http import HttpRequest, HttpResponse
from time import sleep
from random import uniform
from asyncio import sleep as asleep
from .session import Session
from django.views import View

class AsyncView(View):
    session = Session()
    def get(self, request, *args, **kwargs):
        user_email = request.GET.get('email')
        user_email = f"{user_email}@django-poc.com"
        print(f"email {user_email}")
        self.session.set_email(user_email)
        io_time = float(request.GET.get('sleep', 3.9))
        sleep_time = uniform(0, io_time)
        # await asleep(sleep_time)
        print(f"This is my session {self.session}")
        return HttpResponse(f"I napped for {sleep_time} seconds - user {self.session.get_email()}")

def sync_sleep(request):
    sleep_time = uniform(0, 4.9)
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


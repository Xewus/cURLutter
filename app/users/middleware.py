"""Для работы это `middleware` необходимо,
чтоб объект `HttpRequest` содержал `user`
для этого нужно расположить это сразу после
`django.contrib.auth.middleware.AuthenticationMiddleware`.
"""
from django.http.request import HttpRequest

from .models import IP, Agent
from .utils import get_ip_and_agent


class SaveIpAgent:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        if request.user.is_authenticated:
            ip, agent = get_ip_and_agent(request)
            IP.objects.get_or_create(ip=ip, user=request.user)
            Agent.objects.get_or_create(agent=agent, user=request.user)

        return response

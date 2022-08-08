from django.http import HttpRequest


def get_ip_and_agent(request: HttpRequest) -> tuple:
    """Получает `ip` и `user-agent` пользователя.
    """
    user_agent = request.META['HTTP_USER_AGENT']
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not user_ip:
        user_ip = request.META.get('REMOTE_ADDR')
    return user_ip, user_agent

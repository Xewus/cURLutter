from datetime import datetime
from http import HTTPStatus

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import (HttpRequest, HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound)
from django.shortcuts import redirect
from django.views.decorators.http import require_GET

from curlutter.models import Link

url_validator = URLValidator()


@require_GET
def help(request: HttpRequest) -> HttpResponse:
    """Выводит инструкцию по использованию.
    """
    return HttpResponse(f"""
    Чтоб создать короткую ссылку, отправьте "POST"-запрос на ресурс
    {request.build_absolute_uri()}/link/add-link/?short=<>&original=<>&end-time=<>
    Где:
    short - Псевдоним (короткая ссыка).
    original - Оригинальная длинная ссылка.
    end-time - Время действия псевдонима в формате `30-01-2030'.
    Параметр `end-time` опциональный,
    без него время действия ссылки равно времени существования БД.
    """)


@require_GET
def link(request: HttpRequest, short: str) -> HttpResponse:
    """Получает короткую ссылку и перенаправляет на оригинальный ресурс.

    Если запрошенная ссылка просрочена, то удаляет её.

    ### Args:
    - request (HttpRequest):
        Объект запроса.
    - short (str):
        Короткая ссылка.
    """
    link = Link.objects.filter(short=short)[:1]
    if not link:
        return HttpResponseNotFound(f'{short} не найдено')

    if link[0].end_time and (
        link[0].end_time.timestamp() < datetime.now().timestamp()
    ):
        link[0].delete()
        return HttpResponseNotFound(f'{short} удалена')

    return redirect(link[0].original)


@require_GET
def add_link(request: HttpRequest) -> HttpResponse:
    """Добавляет новую короткую ссылку связанную с длинной.

    ### Args:
    - request (HttpRequest):
        Объект запроса.
    """
    short = request.GET.get('short')
    if not short:
        return HttpResponseBadRequest('Не передан параметр `short`')

    if Link.objects.filter(short=short).exists():
        return HttpResponseBadRequest(f'{short} занят')

    original = request.GET.get('original')
    if not original:
        return HttpResponseBadRequest('Не передан параметр `original`')

    try:
        url_validator(original)
    except ValidationError:
        return HttpResponseBadRequest('Некорректный оригинальный адрес')

    end_time = request.GET.get('end-time')
    if end_time:
        try:
            end_time = datetime.strptime(end_time, '%d-%m-%Y')
        except ValueError:
            return HttpResponseBadRequest('Ошибка в параметре `end-time`')

    link = Link(short=short, original=original, end_time=end_time)
    link.save()
    return HttpResponse(
        f'Короткая ссылка "{short}" создана', status=HTTPStatus.ACCEPTED
    )

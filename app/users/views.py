from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse

from user_sessions.backends_db import UserSession


class ChangePasswordView(PasswordChangeView):

    def form_valid(self, form) -> HttpResponse:
        """Удаляет все сессии пользователя при смене пароля.
        """
        UserSession.objects.filter(user_id=self.request.user.id).delete()
        return super().form_valid(form)

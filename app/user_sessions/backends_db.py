from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models


class UserSession(AbstractBaseSession):
    user_id = models.IntegerField(
        verbose_name='id пользователя',
        null=True,
        db_index=True
    )

    @classmethod
    def get_session_store_class(cls):
        return SessionStore


class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return UserSession

    def create_model_instance(
        self, data: dict[str, models.Model]
    ) -> AbstractBaseSession:
        session = super().create_model_instance(data)
        session.user_id = data.get('_auth_user_id')
        return session

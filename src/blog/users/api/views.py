from rest_framework.generics import (
    CreateAPIView,
)

from .serializers import UserRegisterSerializer
from users.models import User


class RegisterAPIView(CreateAPIView):
    """
    Register user with APIs.
    """
    serializer_class = UserRegisterSerializer
    authentication_classes = ()
    permission_classes = ()
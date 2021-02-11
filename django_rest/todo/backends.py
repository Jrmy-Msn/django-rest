import logging
from rest_framework import authentication
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class HeaderAuth(authentication.BaseAuthentication):
    def authenticate(self, request, username = None, password = None):
        user_model = get_user_model()
        credential = {
            'matricule': request.headers.get('matricule'),
            'institution': request.headers.get('institution'),
            'name': request.headers.get('nom'),
        }

        if not credential['matricule']:
            return None

        try:
            user = user_model.objects.get(matricule = credential['matricule'])

        except user_model.DoesNotExist:
            user = user_model(**credential)
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.save()
        return (user, None)

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk = user_id)
        except user_model.DoesNotExist:
            return None
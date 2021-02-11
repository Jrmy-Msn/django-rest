from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, matricule, **credentials):
        if not matricule:
            raise ValueError('Users must have an matricule')

        user = self.model(
            matricule = matricule,
            **credentials
        )
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    matricule = models.CharField(max_length = 6, unique = True)
    institution = models.CharField(max_length = 2)
    name = models.CharField(max_length = 30, blank = True)

    USERNAME_FIELD = 'matricule'
    REQUIRED_FIELDS = ['']

    def __str__(self):
        return '{} ({})'.format(self.name, self.matricule)
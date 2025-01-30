import datetime
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):

    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, null=True)
    email = models.CharField(max_length=100, unique=True, default=None)
    password = models.CharField(default=None, max_length=255)
    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now())
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    def __str__(self):
        return f"id: {self.id}, last_name: {self.last_name}, email: {self.email}"


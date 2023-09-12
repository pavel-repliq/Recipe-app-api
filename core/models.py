from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser

# Create your models here.


class CustomUserManager(BaseUserManager):
    # manager for user for creating user using emails

    def create_user(self, email, password=None, **extra_fields):
        # create , save and return new user
        if not email:
            raise ValueError("email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        #   Create and save a SuperUser with the given email and password.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # user in the system
    username = None
    email = models.EmailField(("email address"), max_length=254, unique=True)
    name = models.CharField(("name"), max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

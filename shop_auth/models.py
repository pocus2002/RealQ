from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class ShopUserManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, nickname, password, **extra_keyword):
        if not email:
            raise ValueError("email must be set.")
        if not nickname:
            raise ValueError("nickname must be set.")
        if not password:
            raise ValueError("password must be set.")
        user = self.model(email=self.normalize_email(email),
                          nickname=nickname,
                          **extra_keyword)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, nickname, password, **extra_keyword):
        extra_keyword.setdefault('is_staff', False)
        extra_keyword.setdefault('is_superuser', False)
        return self._create_user(email, nickname, password, **extra_keyword)
        

    def create_superuser(self, email, nickname, password, **extra_keyword):
        extra_keyword.setdefault('is_staff', True)
        extra_keyword.setdefault('is_superuser', True)
        return self._create_user(email, nickname, password, **extra_keyword)

class ShopUser(AbstractBaseUser, PermissionsMixin):

    objects = ShopUserManager()

    email = models.CharField('email', max_length=256, unique=True, blank=False)
    nickname = models.CharField('nickname', max_length=32, unique=True)
    is_staff = models.BooleanField('staff', default=False)
    is_active = models.BooleanField('active', default=True)
    created_at = models.DateTimeField('created', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname'] # USERNAME_FIELD 와 password 는 기본사항이다.

    def __str__(self):
        return self.nickname
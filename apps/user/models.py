from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    User manager
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a new user
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        if not password:
            raise ValueError('Users must have a password')
        

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and save a new superuser
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Abstract User with the same behaviour as Django's default User.
    AbstractBaseUser - is a base class for creating custom user models.
    PermissionsMixin - is a mixin that adds the ability to check permissions
    """
    email = models.EmailField(max_length=255, unique=True)
    
    avatar = models.ImageField(
        _('Image your profile'),
        upload_to='./',
        null=True,
        default='/profile/default.jpg'
    )
    first_name = models.CharField(
        _('first name'),
        max_length=255,
        blank=True)
    last_name = models.CharField(
        _('last name'),
        max_length=255,
        blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
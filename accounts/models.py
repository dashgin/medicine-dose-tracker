from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from .utils import unique_username_generator


class User(AbstractBaseUser, PermissionsMixin):
    """Default user for {{Medicine Dose Tracker}}."""
    full_name = models.CharField(_('Full Name of User'), max_length=55)
    username = models.CharField(
        _('username'),
        max_length=75,
        null=True,
        blank=True
    )
    email = models.EmailField(
        _('Email of User'),
        unique=True,
        help_text=_('Email of user for login and sending notifications.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        unique_username_generator(instance=self, base_field=self.full_name, new_username=None)
        return super(User, self).save(*args, **kwargs)

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        """
        Get url for user's detail page.
        """
        return reverse('accounts:detail', kwargs={'username': self.username})

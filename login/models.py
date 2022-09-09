from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# create new user
# create superuser

class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise valueError('User must have an email address.')
        if not username:
            raise valueError('User must have an username.')
        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email            = self.normalize_email(email),
            username         = username,
            password         = password,
        )
        user.is_staff    =  True
        user.is_approved =  True

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{profile_image.png}'

def get_default_profile_image_filepath(self):
    return "default/default_profile.png"
def get_student_card_filepath(self):
    return f'profile_images/{str(self.pk)}/{student_card.png}' 

class NewUser(AbstractBaseUser):

    email                = models.EmailField(_('email adress'), unique=True)
    user_name            = models.CharField(max_length=150, unique=True)
    first_name           = models.CharField(max_length=150, unique=False)
    last_name            = models.CharField(max_length=150, unique=False)
    is_student           = models.BooleanField(default=True)
    university           = models.CharField(max_length=150, unique=False, null=True, default=' ')
    level                = models.CharField(max_length=150, unique=False, null=True, default=' ')
    company          = models.CharField(max_length=150, unique=False, null=True, default=' ')

    is_residence         = models.BooleanField(default=False)
    residence            = models.CharField(max_length=150, unique=False, null=True, default=' ')
    is_approved          = models.BooleanField(default=False)

    is_staff             = models.BooleanField(default=False)
    is_active            = models.BooleanField(default=False)

    profile_image        = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, blank=True)
    student_card         = models.ImageField(max_length=255, upload_to=get_student_card_filepath, blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD       = 'email'
    REQUIRED_FIELDS      = ['user_name']



    def __str__(self):
        return self.user_name
    
    def student(self, perm, obj=None):
        return self.is_student

    def is_approved(self, perm, obj=None):
        return self.is_approved

class Resources(models.Model):
        user_publish    = models.ForeignKey(NewUser, on_delete=models.CASCADE)
        module          = models.CharField(max_length=150, unique=False, null=True)
        speciality      = models.CharField(max_length=150, unique=False, null=True)
        level           = models.CharField(max_length=150, unique=False, null=True)
        link            = models.CharField(max_length=150, unique=False, null=True)
        description     = models.CharField(max_length=150, unique=False, null=True)
        created         = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.speciality
        class Meta:
            ordering = ['-created']
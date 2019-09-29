from django.db import models
from PIL import Image
from django.contrib.auth.models import(
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):
    """
    A manager for our custom user model.
    """

    def create_user(self, email, first_name, last_name, password=None):
        #creates a simple user inside our system.
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        #create a super user inside our system.
        user = self.create_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    A user inside our system.
    """

    #info
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #settings
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        fullname = self.first_name+' '+self.last_name
        return fullname
    
    def fullname(self):
        fullname = self.first_name+' '+self.last_name
        return fullname


class Profile(models.Model):
    """
    Users profile to show more infos.
    """
    genders = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)
    address = models .TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=genders, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first
        if self.profile_pic:
            img = Image.open(self.profile_pic.path) # Open image using self

            if img.height > 500 or img.width > 500:
                new_img = (500, 500)
                img.thumbnail(new_img)
                img.save(self.profile_pic.path)  # saving image at the same path

    def __str__(self):
        return self.owner.fullname()
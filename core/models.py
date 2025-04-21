from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",  # Change le nom pour éviter le conflit
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",  # Change aussi ce nom
        blank=True
    )  # Tous les utilisateurs ici seront admin


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class PortfolioProject(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='portfolio_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    # Champs du projet
    owner_name = models.CharField(max_length=255, verbose_name="Nom du Maître d'Ouvrage", null=True, blank=True)
    year = models.PositiveIntegerField(verbose_name="Année", null=True, blank=True)
    surface_area = models.CharField(max_length=100, verbose_name="Surface utile", null=True, blank=True)
    project_status = models.CharField(max_length=255, verbose_name="État d'avancement", null=True, blank=True)
    mission = RichTextField(verbose_name="Missions CIAU", null=True, blank=True)
    budget = models.CharField(max_length=100, null=True, blank=True)

    objectifs = RichTextField(null=True, blank=True)
    approach = RichTextField(null=True, blank=True)

    image_1 = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)

    def __str__(self):
        return self.title




# models.py
class MediaFile(models.Model):
    portfolio_project = models.ForeignKey(
    'PortfolioProject',
    related_name='media_files',
    on_delete=models.CASCADE,
    null=True,  # ✅ Rend le champ nullable
    blank=True  # ✅ Permet de laisser vide dans les formulaires/admin
)
    title = models.CharField(max_length=255, default="Sans titre")
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

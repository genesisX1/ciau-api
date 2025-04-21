from django.contrib import admin
from .models import BlogPost, PortfolioProject, MediaFile
from ckeditor.widgets import CKEditorWidget
from django import forms


class PortfolioProjectAdminForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'objectifs': CKEditorWidget(),
            'approach': CKEditorWidget(),
            'mission': CKEditorWidget(),
        }

class PortfolioProjectAdmin(admin.ModelAdmin):
    form = PortfolioProjectAdminForm

admin.site.register(BlogPost)
admin.site.register(PortfolioProject)
admin.site.register(MediaFile)

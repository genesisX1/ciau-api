from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import BlogPost, PortfolioProject, MediaFile
from ckeditor.widgets import CKEditorWidget
from django import forms



# ==== Admin sécurisé pour User ====

class CustomUserAdmin(BaseUserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_superuser=False)

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if not request.user.is_superuser:
            return tuple(f for f in list_display if f != 'is_superuser')
        return list_display

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            new_fieldsets = []
            for name, options in fieldsets:
                fields = [f for f in options.get("fields", []) if f != "is_superuser"]
                if fields:
                    new_fieldsets.append((name, {"fields": fields}))
            return new_fieldsets
        return fieldsets

    def has_change_permission(self, request, obj=None):
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_view_permission(self, request, obj=None):
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        return super().has_view_permission(request, obj)


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



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(BlogPost)
admin.site.register(PortfolioProject)
admin.site.register(MediaFile)

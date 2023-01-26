from django.contrib import admin

from .models import Post
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)

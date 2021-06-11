from django import forms
from django.db import models
from django.db.models import fields
from .models import Post, Profile , Answer

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["description","topic","img"]

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","name","body","post_at"]

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=["name","question","answer"]
from django import forms
from .models import Comment, Reply
from django.core import validators  # Import the email validator

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['which_blog', 'name', 'email', 'website', 'message']

    # Add validation rules for specific fields
    name = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(validators=[validators.validate_email], required=False)

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['which_comment', 'name', 'message']
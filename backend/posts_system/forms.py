from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Post Title'}),
            'text': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your post content here...'}),
        }
        
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your comment content here...'}),
        }
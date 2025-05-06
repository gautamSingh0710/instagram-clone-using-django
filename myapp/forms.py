
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Enter caption...'})
            }

# from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['image', 'caption']

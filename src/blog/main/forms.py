from django import forms


from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
        attrs={'rows':1, 'cols':10, 'style': 'border-color: blue;', 'placeholder': 'Title.'}), label='')
    content = forms.CharField(widget=forms.Textarea(
        attrs={'rows':4, 'cols':50, 'style': 'border-color: blue;', 'placeholder': 'Write your post here.'}), label='')
    class Meta:
        model = Post
        fields = [
            'title', 'content', 'image'
        ]

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'size':'81', 'style': 'border-color: blue;', 'placeholder': 'Comment ....'}), label='')
    class Meta:
        model = Comment
        fields = [
            'content'
        ]


        attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
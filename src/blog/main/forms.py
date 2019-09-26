from django import forms


from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':50}))
    class Meta:
        model = Post
        fields = [
            'title', 'content', 'image'
        ]

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'size':'60'}))
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
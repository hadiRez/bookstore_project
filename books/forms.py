from django import forms

from .models import Comment, Book


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

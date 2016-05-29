from django import forms
from .models import Comment


class CommentForm(forms.Form):
	author = forms.CharField(max_length=50)
	content = forms.CharField(widget=forms.Textarea)

	def save(self, commit=True):
		comment = Comment(author = self.cleaned_data['author'], content=self.cleaned_data['content'])
		if commit:
			comment.save()
		return comment


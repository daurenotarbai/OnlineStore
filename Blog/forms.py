from django  import forms
from .models import CommentBlog

class AddBlogCommentForm(forms.ModelForm):
  class Meta:
    model =CommentBlog

    fields = ('comment_text',)





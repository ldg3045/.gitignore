from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =  "__all__" # 모든 필드 포함
        # exclude = ("created_at", "updated_at") # 그 중에 제외할 필드 지정


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article",) # 아티클은 제외

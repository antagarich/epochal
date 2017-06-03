from django.forms import ModelForm
from models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article

    def is_valid(self):
        return super(ArticleForm, self).is_valid()
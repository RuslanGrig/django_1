from django.contrib import admin

from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

class BaseScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_count = sum(1 for form in self.forms if form.cleaned_data.get('is_main'))

        if main_count == 0:
            raise ValidationError('Укажите один основной раздел.')
        elif main_count > 1:
            raise ValidationError('Основной раздел может быть только один.')

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = BaseScopeInlineFormSet
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = BaseScopeInlineFormSet
    extra = 1



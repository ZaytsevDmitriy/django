from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scopeship, Tag





class ScopeshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
           if form.cleaned_data.get('is_main'):
               counter += 1
           if counter > 1:
            raise ValidationError('Основной раздел может быть только один.')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeshipInline(admin.TabularInline):
    model = Scopeship
    formset = ScopeshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
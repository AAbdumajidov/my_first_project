from django import forms
from .models import Recipe, Tag, RecipeIngredient


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['id', 'author', 'title', 'tags']
        exclude = ['author']

class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['id', 'author', 'title', 'is_active', 'tags']
        exclude = ['author']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
        exclude = ['recipe']
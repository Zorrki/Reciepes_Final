from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cook_time', 'image', 'categories', 'ingredients']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'rows': 2}),
            'steps': forms.Textarea(attrs={'rows': 4}),
            'ingredients': forms.Textarea(attrs={'rows': 2})
        }
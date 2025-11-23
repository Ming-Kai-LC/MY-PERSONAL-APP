from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Category


class RecipeForm(forms.ModelForm):
    """Form for creating and editing recipes."""

    class Meta:
        model = Recipe
        fields = [
            'title', 'description', 'instructions',
            'prep_time', 'cook_time', 'servings', 'difficulty',
            'categories', 'image', 'notes'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Step-by-step instructions'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutes'}),
            'cook_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutes'}),
            'servings': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of servings'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes or tips'}),
        }


class IngredientForm(forms.ModelForm):
    """Form for individual ingredients."""

    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingredient name'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1, 2, 1/2'}),
            'unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cups, tbsp, grams'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }


# Formset for managing multiple ingredients
IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=5,
    can_delete=True,
    min_num=1,
    validate_min=True,
)

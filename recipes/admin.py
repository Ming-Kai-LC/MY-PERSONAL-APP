from django.contrib import admin
from .models import Recipe, Ingredient, Category


class IngredientInline(admin.TabularInline):
    """Inline admin for ingredients within recipe admin."""
    model = Ingredient
    extra = 3
    fields = ['order', 'quantity', 'unit', 'name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Admin interface for Recipe model."""
    list_display = ['title', 'difficulty', 'prep_time', 'cook_time', 'total_time', 'servings', 'created_at']
    list_filter = ['difficulty', 'categories', 'created_at']
    search_fields = ['title', 'description', 'instructions']
    filter_horizontal = ['categories']
    inlines = [IngredientInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Cooking Details', {
            'fields': ('prep_time', 'cook_time', 'servings', 'difficulty')
        }),
        ('Instructions & Notes', {
            'fields': ('instructions', 'notes')
        }),
        ('Categories', {
            'fields': ('categories',)
        }),
    )

    readonly_fields = []


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Admin interface for Ingredient model."""
    list_display = ['recipe', 'quantity', 'unit', 'name', 'order']
    list_filter = ['recipe']
    search_fields = ['name', 'recipe__title']

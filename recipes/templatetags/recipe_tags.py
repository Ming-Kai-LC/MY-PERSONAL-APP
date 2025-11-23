"""
Custom template tags for recipe app.
Follows Django best practices for reusable components.
"""
from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def difficulty_badge(difficulty, display_text):
    """
    Renders a difficulty badge with appropriate styling.

    Usage: {% difficulty_badge recipe.difficulty recipe.get_difficulty_display %}
    """
    return format_html(
        '<span class="difficulty-badge difficulty-{}">{}</span>',
        difficulty,
        display_text
    )


@register.simple_tag
def time_display(label, time_value, emoji="⏱️"):
    """
    Renders a time display meta item.

    Usage: {% time_display "Prep" recipe.prep_time "⏱️" %}
    """
    return format_html(
        '<span class="meta-item">{} {}: {}m</span>',
        emoji,
        label,
        time_value
    )


@register.filter
def total_time(recipe):
    """
    Calculate total time for a recipe.

    Usage: {{ recipe|total_time }}
    """
    return recipe.prep_time + recipe.cook_time


@register.inclusion_tag('recipes/components/recipe_card.html')
def recipe_card(recipe):
    """
    Renders a recipe card component.

    Usage: {% recipe_card recipe %}
    """
    return {'recipe': recipe}


@register.inclusion_tag('recipes/components/meta_bar.html')
def recipe_meta_bar(recipe):
    """
    Renders recipe metadata bar.

    Usage: {% recipe_meta_bar recipe %}
    """
    return {'recipe': recipe}


@register.filter
def ingredient_display(ingredient):
    """
    Format ingredient for display.

    Usage: {{ ingredient|ingredient_display }}
    """
    unit_str = f" {ingredient.unit}" if ingredient.unit else ""
    return f"{ingredient.quantity}{unit_str} {ingredient.name}"

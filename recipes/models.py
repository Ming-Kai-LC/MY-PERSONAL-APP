from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Recipe categories like Breakfast, Lunch, Dinner, Dessert, etc."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Main recipe model with all details."""
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Brief description of the recipe")
    instructions = models.TextField(help_text="Step-by-step cooking instructions")

    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    servings = models.IntegerField(default=4)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')

    categories = models.ManyToManyField(Category, related_name='recipes', blank=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    notes = models.TextField(blank=True, help_text="Additional notes or tips")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    @property
    def total_time(self):
        """Calculate total cooking time."""
        return self.prep_time + self.cook_time


class Ingredient(models.Model):
    """Ingredients for recipes."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50, help_text="e.g., 2, 1/2, 1.5")
    unit = models.CharField(max_length=50, blank=True, help_text="e.g., cups, tbsp, grams")
    order = models.IntegerField(default=0, help_text="Order of ingredient in the list")

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        unit_str = f" {self.unit}" if self.unit else ""
        return f"{self.quantity}{unit_str} {self.name}"

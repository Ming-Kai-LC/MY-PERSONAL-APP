"""
Unit tests for recipe app.
Follows Django testing best practices.
"""
from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Ingredient, Category


class RecipeModelTest(TestCase):
    """Test Recipe model."""

    def setUp(self):
        """Set up test data."""
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test description",
            instructions="Test instructions",
            prep_time=10,
            cook_time=20,
            servings=4,
            difficulty='easy'
        )

    def test_recipe_creation(self):
        """Test recipe can be created."""
        self.assertEqual(self.recipe.title, "Test Recipe")
        self.assertEqual(self.recipe.prep_time, 10)

    def test_total_time_property(self):
        """Test total_time property calculation."""
        self.assertEqual(self.recipe.total_time, 30)

    def test_recipe_str(self):
        """Test string representation."""
        self.assertEqual(str(self.recipe), "Test Recipe")


class IngredientModelTest(TestCase):
    """Test Ingredient model."""

    def setUp(self):
        """Set up test data."""
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test",
            instructions="Test",
            prep_time=10,
            cook_time=20,
            servings=4
        )
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe,
            name="Flour",
            quantity="2",
            unit="cups",
            order=1
        )

    def test_ingredient_str(self):
        """Test ingredient string representation."""
        self.assertEqual(str(self.ingredient), "2 cups Flour")

    def test_ingredient_without_unit(self):
        """Test ingredient display without unit."""
        ing = Ingredient.objects.create(
            recipe=self.recipe,
            name="Eggs",
            quantity="3",
            unit="",
            order=2
        )
        self.assertEqual(str(ing), "3 Eggs")


class CategoryModelTest(TestCase):
    """Test Category model."""

    def setUp(self):
        """Set up test data."""
        self.category = Category.objects.create(
            name="Breakfast",
            description="Morning meals"
        )

    def test_category_creation(self):
        """Test category creation."""
        self.assertEqual(self.category.name, "Breakfast")

    def test_category_str(self):
        """Test string representation."""
        self.assertEqual(str(self.category), "Breakfast")


class RecipeViewTest(TestCase):
    """Test recipe views."""

    def setUp(self):
        """Set up test client and data."""
        self.client = Client()
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test description",
            instructions="Test instructions",
            prep_time=10,
            cook_time=20,
            servings=4,
            difficulty='easy'
        )

    def test_recipe_list_view(self):
        """Test recipe list view."""
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_recipe_detail_view(self):
        """Test recipe detail view."""
        response = self.client.get(
            reverse('recipe_detail', kwargs={'pk': self.recipe.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_recipe_search(self):
        """Test recipe search functionality."""
        response = self.client.get(reverse('recipe_list'), {'search': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")


class ManagementCommandTest(TestCase):
    """Test management commands."""

    def test_setup_recipes_command(self):
        """Test setup_recipes management command."""
        from django.core.management import call_command
        from io import StringIO

        out = StringIO()
        call_command('setup_recipes', stdout=out)
        self.assertIn('Setup complete', out.getvalue())

        # Check categories were created
        categories = Category.objects.all()
        self.assertGreater(categories.count(), 0)

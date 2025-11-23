# Development Guide

## Django Best Practices Implemented

### 1. DRY (Don't Repeat Yourself)

#### CSS Reusability
- **Common styles** extracted to `static/css/common.css`
- CSS variables for consistent theming
- Reusable component classes

#### Template Tags
- Custom template tags in `recipes/templatetags/recipe_tags.py`
- Reusable components for difficulty badges, time display, etc.
- Usage: `{% load recipe_tags %}`

#### View Mixins
- `SuccessMessageMixin` - Automatic success messages
- `TitleMixin` - Page title management
- `CategoryContextMixin` - Common context data

### 2. Code Organization

```
recipes/
├── models.py           # Data models
├── views.py            # View logic
├── forms.py            # Form definitions
├── mixins.py           # Reusable view mixins
├── admin.py            # Admin configuration
├── urls.py             # URL routing
├── templatetags/       # Custom template tags
│   └── recipe_tags.py
├── management/         # Management commands
│   └── commands/
│       └── setup_recipes.py
└── templates/          # HTML templates
    └── recipes/
```

### 3. Management Commands

Run setup:
```bash
python manage.py setup_recipes
```

Create categories only:
```bash
python manage.py setup_recipes
```

Skip categories:
```bash
python manage.py setup_recipes --skip-categories
```

### 4. Using Template Tags

```django
{% load recipe_tags %}

{# Display difficulty badge #}
{% difficulty_badge recipe.difficulty recipe.get_difficulty_display %}

{# Display time #}
{% time_display "Prep" recipe.prep_time "⏱️" %}

{# Calculate total time #}
{{ recipe|total_time }}

{# Format ingredient #}
{{ ingredient|ingredient_display }}
```

### 5. Using Mixins in Views

```python
from recipes.mixins import SuccessMessageMixin, TitleMixin

class MyView(SuccessMessageMixin, TitleMixin, CreateView):
    success_message = "Recipe created successfully!"
    page_title = "Create Recipe"
```

### 6. Security Best Practices

- ✅ CSRF protection enabled
- ✅ SQL injection prevention (using ORM)
- ✅ XSS protection (template auto-escaping)
- ✅ File upload validation (Pillow)
- ✅ Password validation (Django defaults)

### 7. Performance Optimizations

- **Database**: Use `select_related()` and `prefetch_related()` for foreign keys
- **Templates**: Cache template fragments for heavy pages
- **Static files**: Collected and optimized for production
- **Images**: Pillow for image optimization

### 8. Testing

Run tests:
```bash
python manage.py test recipes
```

Create test:
```python
from django.test import TestCase
from recipes.models import Recipe

class RecipeModelTest(TestCase):
    def test_total_time(self):
        recipe = Recipe(prep_time=10, cook_time=20)
        self.assertEqual(recipe.total_time, 30)
```

### 9. Code Style

- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions/classes
- Keep functions small and focused
- Use type hints where appropriate

### 10. Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Description of changes"

# Push to remote
git push -u origin feature/new-feature
```

## Common Tasks

### Add a new recipe field
1. Update `models.py`
2. Create migration: `python manage.py makemigrations`
3. Run migration: `python manage.py migrate`
4. Update forms and templates

### Add a new category
```python
from recipes.models import Category
Category.objects.create(name="New Category", description="Description")
```

### Export recipes
```bash
python manage.py dumpdata recipes --indent 2 > recipes.json
```

### Import recipes
```bash
python manage.py loaddata recipes.json
```

## Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure production database
- [ ] Set up static file serving
- [ ] Configure media file storage
- [ ] Enable HTTPS
- [ ] Set up error logging
- [ ] Configure backup strategy
- [ ] Set up monitoring

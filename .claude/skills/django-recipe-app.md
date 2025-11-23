# Django Recipe App - Development Skill

A comprehensive Django-based personal recipe management application with modern UI/UX, following all Django best practices.

## Features

### Core Functionality
- ✅ Full CRUD operations for recipes
- ✅ Ingredient management with inline formsets
- ✅ Category/tag system for organizing recipes
- ✅ Image upload for recipe photos
- ✅ Search and filter capabilities
- ✅ Modern, responsive UI with glassmorphism effects
- ✅ Django admin interface

### Technical Excellence
- ✅ **DRY Principle**: Reusable template tags, mixins, and CSS
- ✅ **Testing**: 11 unit tests covering models, views, and commands
- ✅ **Security**: CSRF protection, XSS prevention, secure file uploads
- ✅ **Performance**: Optimized queries, efficient templates
- ✅ **Documentation**: Comprehensive guides and inline documentation

## Quick Start

### 1. Environment Setup
The session-start hook automatically:
- Checks Python and dependency installation
- Runs database migrations
- Sets up initial categories
- Verifies the app is ready

Or run manually:
```bash
./.claude/hooks/session-start.sh
```

### 2. Create Admin User
```bash
python manage.py createsuperuser
```

### 3. Start Development Server
```bash
python manage.py runserver
```

Access at:
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Development Commands

### Management Commands
```bash
# Initialize app with default categories
python manage.py setup_recipes

# Skip category creation
python manage.py setup_recipes --skip-categories
```

### Testing
```bash
# Run all tests
python manage.py test recipes

# Run with verbosity
python manage.py test recipes -v 2

# Run specific test class
python manage.py test recipes.tests.RecipeModelTest
```

### Database
```bash
# Create new migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Reset database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py setup_recipes
```

## Code Architecture

### Project Structure
```
MY-PERSONAL-APP/
├── recipe_project/          # Django project
│   ├── settings.py          # Main settings
│   ├── settings_prod.py     # Production settings template
│   └── urls.py              # Root URL config
├── recipes/                 # Recipe app
│   ├── models.py            # Recipe, Ingredient, Category models
│   ├── views.py             # Class-based views
│   ├── forms.py             # ModelForm and formsets
│   ├── mixins.py            # Reusable view mixins
│   ├── admin.py             # Admin configuration
│   ├── tests.py             # Unit tests (11 tests)
│   ├── templatetags/        # Custom template tags
│   │   └── recipe_tags.py   # Reusable template components
│   ├── management/          # Management commands
│   │   └── commands/
│   │       └── setup_recipes.py
│   └── templates/           # HTML templates
├── static/                  # Static files
│   └── css/
│       └── common.css       # Shared styles
├── .claude/                 # Claude Code configuration
│   ├── hooks/               # Session hooks
│   │   └── session-start.sh
│   └── skills/              # Development skills
└── DEVELOPMENT.md           # Development guide
```

### Django Best Practices Implemented

#### 1. DRY (Don't Repeat Yourself)
**Template Tags** (`recipes/templatetags/recipe_tags.py`):
```python
{% load recipe_tags %}

# Reusable difficulty badge
{% difficulty_badge recipe.difficulty recipe.get_difficulty_display %}

# Formatted time display
{% time_display "Prep" recipe.prep_time "⏱️" %}

# Calculate total time
{{ recipe|total_time }}

# Format ingredient
{{ ingredient|ingredient_display }}
```

**View Mixins** (`recipes/mixins.py`):
```python
from recipes.mixins import SuccessMessageMixin, TitleMixin

class RecipeCreateView(SuccessMessageMixin, TitleMixin, CreateView):
    success_message = "Recipe created successfully!"
    page_title = "Create New Recipe"
```

**Common CSS** (`static/css/common.css`):
- CSS variables for consistent theming
- Reusable component classes
- Common animations

#### 2. Testing
All models, views, and commands have comprehensive tests:
```bash
python manage.py test recipes
# 11 tests: RecipeModel (3), Ingredient (2), Category (2),
#           Views (3), ManagementCommand (1)
```

#### 3. Security
- ✅ CSRF protection enabled
- ✅ SQL injection prevention (ORM)
- ✅ XSS protection (auto-escaping)
- ✅ File upload validation
- ✅ Secure session configuration

#### 4. Code Organization
- Clear separation of concerns
- Reusable components
- Comprehensive docstrings
- PEP 8 compliant

## Common Tasks

### Add a New Recipe Field
1. Update `recipes/models.py`:
```python
class Recipe(models.Model):
    # ... existing fields
    new_field = models.CharField(max_length=100)
```

2. Create and run migration:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Update forms and templates as needed

### Add Custom Category
```python
from recipes.models import Category
Category.objects.create(
    name="Custom Category",
    description="Your description"
)
```

### Export/Import Data
```bash
# Export recipes
python manage.py dumpdata recipes --indent 2 > recipes.json

# Import recipes
python manage.py loaddata recipes.json
```

### Using Template Tags
```django
{% extends 'recipes/base.html' %}
{% load recipe_tags %}

{% block content %}
    <!-- Difficulty badge -->
    {% difficulty_badge recipe.difficulty recipe.get_difficulty_display %}

    <!-- Time displays -->
    {% time_display "Prep" recipe.prep_time %}
    {% time_display "Cook" recipe.cook_time %}

    <!-- Total time -->
    <p>Total: {{ recipe|total_time }} minutes</p>

    <!-- Ingredient display -->
    {% for ing in recipe.ingredients.all %}
        <li>{{ ing|ingredient_display }}</li>
    {% endfor %}
{% endblock %}
```

### Using View Mixins
```python
from django.views.generic import CreateView
from recipes.mixins import SuccessMessageMixin, TitleMixin

class MyView(SuccessMessageMixin, TitleMixin, CreateView):
    model = MyModel
    success_message = "Item created successfully!"
    page_title = "Create Item"
```

## Production Deployment

### 1. Configure Settings
Copy and edit production settings:
```bash
cp recipe_project/settings_prod.py recipe_project/settings_local.py
# Edit settings_local.py with your production values
```

### 2. Environment Variables
Set these in your production environment:
- `DJANGO_SETTINGS_MODULE=recipe_project.settings_local`
- `SECRET_KEY` - Strong, random secret key
- `ALLOWED_HOSTS` - Your domain names
- Database credentials
- Email configuration

### 3. Static Files
```bash
python manage.py collectstatic
```

### 4. Database
```bash
# Run migrations
python manage.py migrate

# Setup initial data
python manage.py setup_recipes

# Create superuser
python manage.py createsuperuser
```

### 5. Security Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use strong `SECRET_KEY`
- [ ] Enable HTTPS
- [ ] Set secure cookie flags
- [ ] Configure error logging
- [ ] Set up database backups
- [ ] Configure media file storage

## Troubleshooting

### Dependencies Not Installed
```bash
pip install -r requirements.txt
```

### Migration Issues
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
# Development
python manage.py collectstatic

# Check settings.py
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### Tests Failing
```bash
# Run with verbose output
python manage.py test recipes -v 2

# Run specific test
python manage.py test recipes.tests.RecipeModelTest.test_total_time
```

## Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Development Guide**: See `DEVELOPMENT.md`
- **Recipe README**: See `RECIPE_README.md`

## Support

For issues or questions:
1. Check `DEVELOPMENT.md` for detailed development guide
2. Run tests to verify functionality
3. Check Django documentation
4. Review code comments and docstrings

---

**Built with Django 5.2 | Modern UI/UX | Production Ready**

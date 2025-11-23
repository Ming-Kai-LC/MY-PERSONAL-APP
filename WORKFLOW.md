# Django Recipe App - Complete Workflow Guide

A step-by-step guide for using your Django recipe management system.

---

## 🚀 First Time Setup (One-Time Only)

### Step 1: Start Claude Code Session
When you open this project in Claude Code, the session-start hook automatically:
- ✅ Checks dependencies
- ✅ Runs migrations
- ✅ Sets up 12 default categories
- ✅ Verifies everything is ready

**You'll see:**
```
✅ Django Recipe App is ready!
```

### Step 2: Create Your Admin Account
```bash
python manage.py createsuperuser
```

**Enter:**
- Username: `admin` (or your preferred username)
- Email: (optional, press Enter to skip)
- Password: (enter a secure password)

### Step 3: Start the Server
```bash
python manage.py runserver
```

### Step 4: Access Your App
Open your browser:
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

**✅ Setup Complete!** You're ready to start adding recipes.

---

## 📖 Daily Workflow

### Starting Your Day

1. **Start Claude Code session** (hook runs automatically)
2. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
3. **Open your browser** to http://127.0.0.1:8000/

### Stopping Your Work

1. **Stop the server:** Press `Ctrl+C` in terminal
2. **Commit changes** (if you made any code changes):
   ```bash
   git add .
   git commit -m "Your commit message"
   git push
   ```

---

## 🍳 Recipe Management Workflows

### Adding a New Recipe

#### **Method 1: Web Interface (Recommended)**

1. **Click "+ Add Recipe"** button on homepage
2. **Fill in the form:**
   - **Title**: "Chocolate Chip Cookies"
   - **Description**: "Classic homemade cookies"
   - **Prep Time**: 15 (minutes)
   - **Cook Time**: 12 (minutes)
   - **Servings**: 24
   - **Difficulty**: Easy
3. **Add Ingredients** (fill in as many rows as needed):
   - Name: "Flour", Quantity: "2", Unit: "cups", Order: 1
   - Name: "Sugar", Quantity: "1", Unit: "cup", Order: 2
   - Name: "Chocolate chips", Quantity: "2", Unit: "cups", Order: 3
4. **Write Instructions** (step-by-step):
   ```
   1. Preheat oven to 375°F
   2. Mix dry ingredients
   3. Add wet ingredients
   4. Fold in chocolate chips
   5. Bake for 12 minutes
   ```
5. **Add Notes** (optional):
   ```
   Store in airtight container for up to 1 week
   ```
6. **Select Categories**: Check "Dessert", "Quick & Easy"
7. **Upload Photo** (optional): Choose recipe image
8. **Click "Create Recipe"**

#### **Method 2: Admin Panel**

1. Go to http://127.0.0.1:8000/admin/
2. Login with your credentials
3. Click **"Recipes"** → **"Add Recipe"**
4. Fill in all fields
5. **Inline Ingredients**: Add ingredients directly in the same form
6. **Save**

### Viewing Recipes

#### **Browse All Recipes**
- Go to homepage: http://127.0.0.1:8000/
- See beautiful card grid with all recipes
- Hover over cards for animation effects

#### **Search for Recipes**
1. Use search bar on homepage
2. Search by:
   - Recipe name: "cookies"
   - Ingredient: "chocolate"
   - Description keywords

#### **Filter Recipes**
1. Use dropdown filters:
   - **Category**: Select "Dessert", "Italian", etc.
   - **Difficulty**: Easy, Medium, or Hard
2. Combine search + filters for precise results

#### **View Recipe Details**
1. Click on any recipe card
2. See:
   - Full recipe details
   - Ingredient list
   - Step-by-step instructions
   - Time information
   - Notes and tips

### Editing a Recipe

1. **Open recipe detail page**
2. **Click "Edit Recipe"** button
3. **Modify any fields**
4. **Update ingredients** (add/remove/edit)
5. **Click "Update Recipe"**

### Deleting a Recipe

1. **Open recipe detail page**
2. **Click "Delete Recipe"** button
3. **Confirm deletion** (warning: cannot be undone!)

---

## 🏷️ Category Management

### View All Categories
```bash
# Via Django shell
python manage.py shell
>>> from recipes.models import Category
>>> Category.objects.all()
```

### Add New Category

#### **Method 1: Admin Panel**
1. Go to http://127.0.0.1:8000/admin/
2. Click **"Categories"** → **"Add Category"**
3. Enter name: "Keto"
4. Enter description: "Low-carb ketogenic recipes"
5. Save

#### **Method 2: Management Command**
```python
python manage.py shell
>>> from recipes.models import Category
>>> Category.objects.create(name="Keto", description="Low-carb recipes")
```

### Default Categories
The system includes 12 categories:
- Breakfast, Lunch, Dinner, Dessert
- Snacks, Italian, Mexican, Asian
- Vegan, Vegetarian, Quick & Easy, Healthy

---

## 🧪 Testing Workflow

### Run All Tests
```bash
python manage.py test recipes
```

**Expected output:**
```
Ran 11 tests in 0.062s
OK
```

### Run Specific Test
```bash
# Test recipe model only
python manage.py test recipes.tests.RecipeModelTest

# Test specific method
python manage.py test recipes.tests.RecipeModelTest.test_total_time
```

### Run Tests with Verbose Output
```bash
python manage.py test recipes -v 2
```

### When to Run Tests
- ✅ Before committing code changes
- ✅ After adding new features
- ✅ After modifying models
- ✅ Before deploying to production

---

## 💻 Development Workflows

### Making Code Changes

#### **Example: Add a New Recipe Field**

1. **Update the model** (`recipes/models.py`):
   ```python
   class Recipe(models.Model):
       # ... existing fields
       source = models.CharField(max_length=200, blank=True)  # NEW
   ```

2. **Create migration:**
   ```bash
   python manage.py makemigrations
   ```

3. **Review migration:**
   ```bash
   cat recipes/migrations/0002_recipe_source.py
   ```

4. **Apply migration:**
   ```bash
   python manage.py migrate
   ```

5. **Update forms** (`recipes/forms.py`):
   ```python
   class RecipeForm(forms.ModelForm):
       class Meta:
           fields = [..., 'source']  # Add to fields list
   ```

6. **Update templates** (add source field to display/form)

7. **Run tests:**
   ```bash
   python manage.py test recipes
   ```

8. **Commit changes:**
   ```bash
   git add .
   git commit -m "Add source field to recipes"
   git push
   ```

### Resetting Database (Development Only)

```bash
# Delete database
rm db.sqlite3

# Recreate from migrations
python manage.py migrate

# Setup initial data
python manage.py setup_recipes

# Create admin user again
python manage.py createsuperuser
```

### Backup Your Data

#### **Export Recipes**
```bash
python manage.py dumpdata recipes.Recipe recipes.Ingredient > my_recipes.json
```

#### **Import Recipes**
```bash
python manage.py loaddata my_recipes.json
```

#### **Backup Database File**
```bash
cp db.sqlite3 db.sqlite3.backup
```

#### **Backup Media Files**
```bash
cp -r media media_backup
```

---

## 🎨 Customization Workflows

### Change Color Scheme

Edit `recipes/templates/recipes/base.html`:
```css
:root {
    --primary: #6366f1;      /* Change to your color */
    --secondary: #ec4899;    /* Change to your color */
    /* ... */
}
```

### Add Custom Template Tag

1. **Create tag** in `recipes/templatetags/recipe_tags.py`:
   ```python
   @register.filter
   def my_custom_filter(value):
       return value.upper()
   ```

2. **Use in template:**
   ```django
   {% load recipe_tags %}
   {{ recipe.title|my_custom_filter }}
   ```

### Add Custom Management Command

1. **Create file:** `recipes/management/commands/my_command.py`
2. **Define command:**
   ```python
   from django.core.management.base import BaseCommand

   class Command(BaseCommand):
       help = 'My custom command'

       def handle(self, *args, **options):
           self.stdout.write('Hello!')
   ```

3. **Run command:**
   ```bash
   python manage.py my_command
   ```

---

## 📊 Data Management Workflows

### View Database in Django Shell

```bash
python manage.py shell
```

**Common queries:**
```python
# Import models
from recipes.models import Recipe, Ingredient, Category

# Count recipes
Recipe.objects.count()

# Get all recipes
recipes = Recipe.objects.all()

# Get recipes by difficulty
easy_recipes = Recipe.objects.filter(difficulty='easy')

# Get recipes with specific ingredient
chocolate_recipes = Recipe.objects.filter(
    ingredients__name__icontains='chocolate'
).distinct()

# Get recipes by category
desserts = Recipe.objects.filter(categories__name='Dessert')

# Get recipe with ingredients
recipe = Recipe.objects.get(id=1)
for ing in recipe.ingredients.all():
    print(ing)
```

### Bulk Import Recipes

Create `import_recipes.py`:
```python
from recipes.models import Recipe, Ingredient, Category

# Create category
dessert = Category.objects.get(name='Dessert')

# Create recipe
recipe = Recipe.objects.create(
    title="Brownies",
    description="Fudgy chocolate brownies",
    instructions="1. Mix\n2. Bake\n3. Enjoy",
    prep_time=10,
    cook_time=25,
    servings=12,
    difficulty='easy'
)

# Add ingredients
Ingredient.objects.create(recipe=recipe, name="Cocoa", quantity="1", unit="cup", order=1)
Ingredient.objects.create(recipe=recipe, name="Sugar", quantity="2", unit="cups", order=2)

# Add categories
recipe.categories.add(dessert)
```

Run: `python manage.py shell < import_recipes.py`

---

## 🚢 Production Deployment Workflow

### 1. Prepare for Production

**Update settings:**
```bash
cp recipe_project/settings_prod.py recipe_project/settings_local.py
# Edit settings_local.py with production values
```

**Set environment variables:**
```bash
export DJANGO_SETTINGS_MODULE=recipe_project.settings_local
export SECRET_KEY="your-secret-key"
```

### 2. Collect Static Files

```bash
python manage.py collectstatic
```

### 3. Run Production Checks

```bash
python manage.py check --deploy
```

### 4. Setup Production Database

```bash
# Run migrations
python manage.py migrate

# Setup initial data
python manage.py setup_recipes

# Create admin user
python manage.py createsuperuser
```

### 5. Configure Web Server

Use Gunicorn or uWSGI with Nginx/Apache.

**Example with Gunicorn:**
```bash
pip install gunicorn
gunicorn recipe_project.wsgi:application --bind 0.0.0.0:8000
```

---

## 🔧 Troubleshooting Workflows

### Server Won't Start

1. **Check if port is in use:**
   ```bash
   lsof -i :8000
   ```

2. **Use different port:**
   ```bash
   python manage.py runserver 8001
   ```

3. **Check for errors:**
   ```bash
   python manage.py check
   ```

### Migrations Not Working

1. **Check migration status:**
   ```bash
   python manage.py showmigrations
   ```

2. **Fake migration (if needed):**
   ```bash
   python manage.py migrate --fake recipes
   ```

3. **Reset migrations (development only):**
   ```bash
   rm recipes/migrations/0*.py
   python manage.py makemigrations recipes
   python manage.py migrate
   ```

### Tests Failing

1. **Run with verbose output:**
   ```bash
   python manage.py test recipes -v 2
   ```

2. **Check specific test:**
   ```bash
   python manage.py test recipes.tests.RecipeModelTest.test_total_time
   ```

3. **Check database:**
   ```bash
   python manage.py dbshell
   ```

### Images Not Displaying

1. **Check MEDIA_URL in settings:**
   ```python
   MEDIA_URL = "media/"
   MEDIA_ROOT = BASE_DIR / "media"
   ```

2. **Check URL configuration:**
   ```python
   # recipe_project/urls.py
   from django.conf.urls.static import static
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

3. **Verify media directory exists:**
   ```bash
   ls -la media/
   ```

---

## ✅ Quick Reference

### Most Common Commands

```bash
# Development
python manage.py runserver          # Start server
python manage.py test recipes       # Run tests
python manage.py createsuperuser    # Create admin

# Database
python manage.py makemigrations     # Create migrations
python manage.py migrate            # Apply migrations
python manage.py setup_recipes      # Setup categories

# Data Management
python manage.py shell              # Django shell
python manage.py dumpdata recipes   # Export data
python manage.py loaddata file.json # Import data

# Verification
python manage.py check              # System check
./.claude/hooks/session-start.sh    # Re-run setup
```

### Key URLs

- **Homepage**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/
- **Add Recipe**: http://127.0.0.1:8000/recipe/new/

### Important Files

- **Models**: `recipes/models.py`
- **Views**: `recipes/views.py`
- **Forms**: `recipes/forms.py`
- **Templates**: `recipes/templates/recipes/`
- **Tests**: `recipes/tests.py`
- **Settings**: `recipe_project/settings.py`

---

## 📚 Next Steps

1. **Add your first recipe** using the web interface
2. **Customize categories** for your cooking style
3. **Upload recipe photos** to make it visually appealing
4. **Explore the admin panel** for advanced management
5. **Run tests** to ensure everything works
6. **Backup your data** regularly

---

**Need Help?**
- Check `DEVELOPMENT.md` for technical details
- Review `.claude/skills/django-recipe-app.md` for comprehensive guide
- Run `python manage.py help` for Django commands

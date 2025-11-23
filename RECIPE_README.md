# Personal Recipe Book 🍳

A beautiful, modern Django web application for storing and managing your personal recipe collection. Keep all your favorite recipes organized in one place with an elegant, user-friendly interface.

## Features

### Core Functionality
- ✅ **Create, Read, Update, Delete (CRUD) recipes**
- 🖼️ **Upload recipe images**
- 📝 **Detailed recipe information**:
  - Title and description
  - Prep time and cook time
  - Number of servings
  - Difficulty level (Easy, Medium, Hard)
  - Step-by-step instructions
  - Additional notes and tips
- 🛒 **Ingredient management** with quantities and units
- 🏷️ **Categories/tags** for organizing recipes
- 🔍 **Search functionality** by recipe name, description, or ingredients
- 🎯 **Filter recipes** by category and difficulty
- 📱 **Responsive design** - works on desktop and mobile
- 🎨 **Clean, modern interface** with gradient accents

### Admin Panel
- Full-featured Django admin interface
- Inline ingredient editing within recipes
- Category management
- Search and filter capabilities

## Tech Stack

- **Django 5.2** - Python web framework
- **SQLite** - Database (file-based, no setup required)
- **Pillow** - Image processing
- **Pure HTML/CSS** - No external CSS frameworks needed

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Django and Pillow.

### Step 2: Database Setup

The database is already initialized! If you need to reset it:

```bash
python manage.py migrate
```

### Step 3: Create Admin Account

Create your admin account to access the admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email (optional)
- Password

### Step 4: Run the Server

```bash
python manage.py runserver
```

The application will be available at:
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Usage Guide

### Adding Your First Recipe

1. **Via Web Interface**:
   - Click the "+ Add Recipe" button
   - Fill in the recipe details
   - Add ingredients (at least one required)
   - Click "Create Recipe"

2. **Via Admin Panel**:
   - Go to http://127.0.0.1:8000/admin/
   - Log in with your superuser credentials
   - Navigate to "Recipes" → "Add Recipe"
   - Fill in details and add ingredients inline
   - Save

### Managing Categories

Categories help organize your recipes (e.g., Breakfast, Lunch, Dinner, Dessert, Italian, Vegan).

1. Go to the Admin Panel: http://127.0.0.1:8000/admin/
2. Click "Categories" → "Add Category"
3. Enter category name and optional description
4. Save

### Searching Recipes

Use the search bar on the homepage to:
- Search by recipe title
- Search by description
- Search by ingredient names

### Filtering Recipes

Use the filter dropdowns to:
- Filter by category
- Filter by difficulty level
- Combine filters with search

## Project Structure

```
MY-PERSONAL-APP/
├── recipe_project/          # Django project settings
│   ├── settings.py          # Configuration
│   ├── urls.py              # Main URL routing
│   └── ...
├── recipes/                 # Recipe app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Forms
│   ├── admin.py             # Admin configuration
│   ├── urls.py              # App URL routing
│   ├── templates/           # HTML templates
│   │   └── recipes/
│   │       ├── base.html
│   │       ├── recipe_list.html
│   │       ├── recipe_detail.html
│   │       ├── recipe_form.html
│   │       └── recipe_confirm_delete.html
│   └── migrations/          # Database migrations
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User uploaded files
│   └── recipe_images/       # Recipe images
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Database Models

### Recipe
- Title, description, instructions
- Prep time, cook time, servings
- Difficulty level
- Image upload
- Categories (many-to-many)
- Notes
- Timestamps (created, updated)

### Ingredient
- Name, quantity, unit
- Order (for sorting)
- Linked to recipe

### Category
- Name, description
- Timestamps

## Tips & Best Practices

1. **Images**: For best results, use images with a 4:3 or 16:9 aspect ratio
2. **Instructions**: Write step-by-step instructions, each on a new line for clarity
3. **Ingredients**: List ingredients in the order they're used
4. **Categories**: Create categories before adding recipes to organize them from the start
5. **Backup**: Regularly backup your `db.sqlite3` file and `media/` folder

## Common Tasks

### Backup Your Data

```bash
# Backup database
cp db.sqlite3 db.sqlite3.backup

# Backup uploaded images
cp -r media media_backup
```

### Reset Database (WARNING: Deletes all data)

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Add Sample Categories

Via Django shell:
```bash
python manage.py shell
```

Then:
```python
from recipes.models import Category

categories = ['Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Snacks',
              'Italian', 'Mexican', 'Asian', 'Vegan', 'Quick & Easy']

for cat in categories:
    Category.objects.get_or_create(name=cat)
```

## Troubleshooting

### Images not displaying
- Ensure `media/` directory exists
- Check that DEBUG=True in settings.py for development
- Verify image was uploaded successfully

### Can't access admin panel
- Create a superuser: `python manage.py createsuperuser`
- Make sure you're using the correct credentials

### Database errors
- Run migrations: `python manage.py migrate`
- Check that db.sqlite3 file exists

## Future Enhancement Ideas

- Recipe ratings and favorites
- Print-friendly recipe view
- Export recipes to PDF
- Shopping list generator
- Meal planning calendar
- Recipe import from URLs
- Nutrition information
- Cooking timer integration

## License

This is a personal project. Feel free to use and modify as you wish!

## Credits

Built with Django - The web framework for perfectionists with deadlines.

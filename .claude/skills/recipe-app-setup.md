# Recipe App Development Setup - Session Start Hook

This skill automatically sets up the Django recipe app development environment when a Claude Code session starts.

## Automatic Setup

When you start a Claude Code session, the session-start hook (`.claude/hooks/session-start.sh`) automatically:

1. ✅ Checks Python version
2. ✅ Verifies Django and Pillow are installed
3. ✅ Installs dependencies if missing
4. ✅ Runs database migrations if needed
5. ✅ Sets up initial recipe categories (12 default categories)
6. ✅ Runs Django system checks
7. ✅ Displays quick reference commands

## Manual Setup

If you need to run the setup manually:

```bash
./.claude/hooks/session-start.sh
```

## What Gets Installed

### Dependencies
- **Django 5.2** - Web framework
- **Pillow** - Image processing

### Initial Data
12 default recipe categories:
- Breakfast, Lunch, Dinner, Dessert
- Snacks, Italian, Mexican, Asian
- Vegan, Vegetarian, Quick & Easy, Healthy

## Next Steps

After setup completes:

### 1. Create Admin User (First Time Only)
```bash
python manage.py createsuperuser
```

### 2. Start Development Server
```bash
python manage.py runserver
```

### 3. Access the Application
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Quick Commands

```bash
# Run tests
python manage.py test recipes

# Setup/reset categories
python manage.py setup_recipes

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Troubleshooting

### Hook Not Running
Make sure the hook is executable:
```bash
chmod +x .claude/hooks/session-start.sh
```

### Dependencies Not Installing
Manually install:
```bash
pip install -r requirements.txt
```

### Database Issues
Reset and re-migrate:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py setup_recipes
```

## Environment Ready Indicators

When setup is complete, you should see:
```
✅ Django Recipe App is ready!

Quick commands:
  🚀 Start server:     python manage.py runserver
  👤 Create admin:     python manage.py createsuperuser
  🧪 Run tests:        python manage.py test recipes
  📊 Setup data:       python manage.py setup_recipes

Access your app:
  📱 Main app:         http://127.0.0.1:8000/
  ⚙️  Admin panel:      http://127.0.0.1:8000/admin/
```

## More Information

For comprehensive development guide, see:
- **Main Skill**: `.claude/skills/django-recipe-app.md`
- **Development Guide**: `DEVELOPMENT.md`
- **User Guide**: `RECIPE_README.md`


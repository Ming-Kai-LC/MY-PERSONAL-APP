# Recipe App Development Setup

This skill automatically sets up the Django recipe app development environment when a session starts.

## What it does:

1. Checks if dependencies are installed
2. Runs database migrations if needed
3. Sets up initial categories
4. Verifies the app is ready to run

## Setup Tasks

### Check Dependencies
```bash
python --version
pip show Django Pillow
```

### Database Setup
```bash
# Run migrations if needed
python manage.py migrate --check || python manage.py migrate

# Setup initial data
python manage.py setup_recipes
```

### Verification
```bash
# Check if server can start
python manage.py check --deploy
```

## Environment Ready

Once setup is complete, you can:
- Run the development server: `python manage.py runserver`
- Access the app at: http://127.0.0.1:8000/
- Access admin at: http://127.0.0.1:8000/admin/

## Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

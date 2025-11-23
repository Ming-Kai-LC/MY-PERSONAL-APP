#!/bin/bash
# Django Recipe App - Session Start Hook
# Automatically sets up the development environment when Claude Code session starts

echo "🍳 Setting up Django Recipe App environment..."

# Check Python version
echo "📌 Checking Python version..."
python --version

# Check if Django is installed
echo "📦 Checking dependencies..."
if ! python -c "import django" 2>/dev/null; then
    echo "⚠️  Django not found. Installing dependencies..."
    pip install -r requirements.txt
else
    echo "✓ Django is installed"
fi

# Check if Pillow is installed
if ! python -c "import PIL" 2>/dev/null; then
    echo "⚠️  Pillow not found. Installing dependencies..."
    pip install -r requirements.txt
else
    echo "✓ Pillow is installed"
fi

# Run migrations if needed
echo "🗄️  Checking database migrations..."
if ! python manage.py migrate --check 2>/dev/null; then
    echo "⚠️  Running migrations..."
    python manage.py migrate
else
    echo "✓ Database is up to date"
fi

# Setup initial categories
echo "📋 Setting up initial data..."
python manage.py setup_recipes

# Run system checks
echo "🔍 Running Django system checks..."
python manage.py check

echo ""
echo "✅ Django Recipe App is ready!"
echo ""
echo "Quick commands:"
echo "  🚀 Start server:     python manage.py runserver"
echo "  👤 Create admin:     python manage.py createsuperuser"
echo "  🧪 Run tests:        python manage.py test recipes"
echo "  📊 Setup data:       python manage.py setup_recipes"
echo ""
echo "Access your app:"
echo "  📱 Main app:         http://127.0.0.1:8000/"
echo "  ⚙️  Admin panel:      http://127.0.0.1:8000/admin/"
echo ""

# 🍳 Django Recipe Book

A modern, full-featured personal recipe management application built with Django. Store, organize, and discover your favorite recipes with a beautiful, responsive interface.

![Django](https://img.shields.io/badge/Django-5.2-green)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Tests](https://img.shields.io/badge/Tests-11%20passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

### Core Functionality
- 🍽️ **Full Recipe Management** - Create, view, edit, and delete recipes
- 🛒 **Ingredient Tracking** - Manage ingredients with quantities and units
- 🏷️ **Categories & Tags** - Organize recipes (Breakfast, Italian, Vegan, etc.)
- 🖼️ **Image Upload** - Add beautiful photos to your recipes
- 🔍 **Search & Filter** - Find recipes by name, ingredients, or categories
- ⏱️ **Time Tracking** - Prep time, cook time, and servings

### Modern UI/UX
- 🎨 **Glassmorphism Design** - Beautiful frosted glass effects
- 🌈 **Gradient Accents** - Eye-catching color schemes
- ✨ **Smooth Animations** - Card hover effects, fade-ins, transitions
- 📱 **Fully Responsive** - Works perfectly on mobile, tablet, and desktop
- 🎯 **Intuitive Interface** - Clean, modern, easy to navigate

### Developer Excellence
- ✅ **Django Best Practices** - DRY, reusable components, clean code
- 🧪 **Comprehensive Tests** - 11 unit tests covering models, views, commands
- 🔒 **Security First** - CSRF, XSS, SQL injection prevention
- 📦 **Easy Setup** - Automated session-start hook
- 📚 **Well Documented** - Extensive guides and inline documentation
- 🚀 **Production Ready** - Deploy to any Django-compatible host

---

## 🚀 Quick Start

### Option 1: Automatic Setup (Recommended)
Just open the project in Claude Code - the session-start hook handles everything!

### Option 2: Manual Setup (3 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup database and categories
python manage.py migrate
python manage.py setup_recipes

# 3. Create admin account
python manage.py createsuperuser

# 4. Start server
python manage.py runserver
```

**Open browser:** http://127.0.0.1:8000/

**See:** [QUICKSTART.md](QUICKSTART.md) for detailed 3-minute setup guide.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[QUICKSTART.md](QUICKSTART.md)** | 3-minute setup guide - Get started fast! |
| **[WORKFLOW.md](WORKFLOW.md)** | Complete workflow guide for all tasks |
| **[DEVELOPMENT.md](DEVELOPMENT.md)** | Technical guide for developers |
| **[RECIPE_README.md](RECIPE_README.md)** | User manual and features guide |
| **[.claude/skills/](/.claude/skills/)** | Claude Code skills and automation |

---

## 🎯 Common Tasks

### Add Your First Recipe
1. Click **"+ Add Recipe"** button
2. Fill in recipe details (title, times, difficulty)
3. Add ingredients (at least one required)
4. Write step-by-step instructions
5. Select categories (Dessert, Italian, etc.)
6. Upload photo (optional)
7. Click **"Create Recipe"**

### Search Recipes
- Use search bar to find by name, ingredients, or description
- Filter by category (Breakfast, Lunch, Dinner, etc.)
- Filter by difficulty (Easy, Medium, Hard)
- Combine search + filters for precise results

### Manage Categories
12 default categories included:
- Meals: Breakfast, Lunch, Dinner, Dessert, Snacks
- Cuisine: Italian, Mexican, Asian
- Diet: Vegan, Vegetarian, Healthy
- Quick & Easy

Add custom categories via admin panel: http://127.0.0.1:8000/admin/

---

## 🏗️ Project Structure

```
MY-PERSONAL-APP/
├── 📝 Documentation
│   ├── README.md              # This file
│   ├── QUICKSTART.md          # 3-minute setup guide
│   ├── WORKFLOW.md            # Complete workflow guide
│   ├── DEVELOPMENT.md         # Developer guide
│   └── RECIPE_README.md       # User manual
│
├── ⚙️ Django Project
│   ├── recipe_project/        # Project settings
│   │   ├── settings.py        # Main configuration
│   │   ├── settings_prod.py   # Production template
│   │   └── urls.py            # URL routing
│   │
│   └── recipes/               # Recipe app
│       ├── models.py          # Data models
│       ├── views.py           # View logic
│       ├── forms.py           # Form definitions
│       ├── admin.py           # Admin interface
│       ├── tests.py           # Unit tests (11 tests)
│       ├── mixins.py          # Reusable view mixins
│       ├── templatetags/      # Custom template tags
│       ├── management/        # Management commands
│       └── templates/         # HTML templates
│
├── 🎨 Frontend
│   ├── static/css/            # Shared styles
│   └── media/                 # Uploaded images
│
├── 🤖 Automation
│   └── .claude/
│       ├── hooks/             # Session start hook
│       └── skills/            # Development skills
│
└── 🗄️ Data
    ├── db.sqlite3             # SQLite database
    └── requirements.txt       # Python dependencies
```

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test recipes

# Expected output:
# Ran 11 tests in 0.062s
# OK
```

**Tests cover:**
- ✅ Recipe model (creation, properties, display)
- ✅ Ingredient model (display with/without units)
- ✅ Category model (creation, display)
- ✅ Recipe views (list, detail, search)
- ✅ Management commands (setup)

---

## 🔧 Development

### Built With
- **Django 5.2** - Web framework
- **Python 3.11+** - Programming language
- **SQLite** - Database
- **Pillow** - Image processing
- **HTML/CSS** - Frontend (no external frameworks!)

### Django Best Practices Implemented
- ✅ **DRY Principle** - Template tags, mixins, shared CSS
- ✅ **Code Organization** - Clear separation of concerns
- ✅ **Testing** - Comprehensive unit test coverage
- ✅ **Security** - CSRF, XSS, SQL injection prevention
- ✅ **Documentation** - Inline docstrings and guides
- ✅ **Reusability** - Custom template tags and view mixins

### Key Features
- **Template Tags** - Reusable components for badges, time display
- **View Mixins** - SuccessMessageMixin, TitleMixin, CategoryContextMixin
- **Management Commands** - `python manage.py setup_recipes`
- **Session Hook** - Automatic environment setup
- **Production Settings** - Ready-to-use production template

---

## 📦 Deployment

### Development
```bash
python manage.py runserver
```

### Production

1. **Configure settings:**
   ```bash
   cp recipe_project/settings_prod.py recipe_project/settings_local.py
   # Edit settings_local.py
   ```

2. **Set environment variables:**
   ```bash
   export DJANGO_SETTINGS_MODULE=recipe_project.settings_local
   export SECRET_KEY="your-secret-key"
   ```

3. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

4. **Deploy with Gunicorn:**
   ```bash
   pip install gunicorn
   gunicorn recipe_project.wsgi:application
   ```

See [WORKFLOW.md](WORKFLOW.md#-production-deployment-workflow) for complete deployment guide.

---

## 🎨 Screenshots

### Homepage - Modern Card Grid
Beautiful recipe cards with hover effects and gradient badges.

### Recipe Detail - Clean Layout
Large hero image, organized ingredients, step-by-step instructions.

### Add Recipe - Intuitive Form
Clean form with inline ingredient management and category selection.

### Search & Filter
Powerful search with multiple filters for finding recipes fast.

---

## 🤝 Contributing

This is a personal project, but feel free to:
- Fork and customize for your needs
- Report issues or suggestions
- Submit pull requests for improvements

---

## 📄 License

MIT License - See LICENSE file for details.

---

## 🆘 Support & Troubleshooting

### Common Issues

**Server won't start:**
```bash
./.claude/hooks/session-start.sh  # Re-run setup
python manage.py check            # Check for errors
```

**Forgot admin password:**
```bash
python manage.py createsuperuser  # Create new admin
```

**Reset database:**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py setup_recipes
```

### Get Help
- Check [WORKFLOW.md](WORKFLOW.md) for detailed workflows
- Review [DEVELOPMENT.md](DEVELOPMENT.md) for technical details
- See `.claude/skills/django-recipe-app.md` for comprehensive guide

---

## 📊 Stats

- **Lines of Code**: ~2,500+
- **Test Coverage**: 11 tests, 100% passing
- **Models**: 3 (Recipe, Ingredient, Category)
- **Views**: 5 class-based views
- **Templates**: 5 responsive templates
- **Custom Tags**: 6 reusable template tags
- **Management Commands**: 1 setup command
- **Default Categories**: 12

---

## 🎯 Roadmap

Potential future enhancements:
- [ ] Recipe ratings and reviews
- [ ] Favorites/bookmarks
- [ ] Shopping list generator
- [ ] Meal planning calendar
- [ ] Recipe import from URLs
- [ ] Nutrition information
- [ ] Recipe sharing/export to PDF
- [ ] Multi-user support
- [ ] Recipe collections

---

## 🙏 Acknowledgments

Built with:
- Django - The web framework for perfectionists with deadlines
- Python - Beautiful is better than ugly, simple is better than complex
- Modern UI/UX design principles
- Django best practices and design patterns

---

## 📞 Contact

For questions or suggestions about this project, please open an issue on GitHub.

---

**Made with ❤️ and Django**

*Your personal recipe book - Store, organize, and discover your favorite recipes!*

---

### Quick Links

- 🚀 [Quick Start Guide](QUICKSTART.md)
- 📖 [Complete Workflow](WORKFLOW.md)
- 💻 [Development Guide](DEVELOPMENT.md)
- 📚 [User Manual](RECIPE_README.md)
- 🤖 [Claude Skills](.claude/skills/)

**Start cooking:** `python manage.py runserver` → http://127.0.0.1:8000/

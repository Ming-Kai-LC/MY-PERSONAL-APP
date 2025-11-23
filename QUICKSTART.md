# Quick Start Guide - Get Cooking in 3 Minutes! 🍳

The fastest way to get your Django recipe app running.

---

## ⚡ 3-Minute Setup

### Step 1: Start Claude Code ✅
**The session hook does everything automatically!**

When you opened this project, it already:
- ✅ Checked Python & dependencies
- ✅ Ran database migrations
- ✅ Created 12 recipe categories
- ✅ Verified the system

### Step 2: Create Admin Account (30 seconds)
```bash
python manage.py createsuperuser
```

**Enter when prompted:**
- Username: `admin`
- Email: *(just press Enter to skip)*
- Password: *(choose a password)*

### Step 3: Start the Server (10 seconds)
```bash
python manage.py runserver
```

### Step 4: Open Your Browser 🚀
Click: **http://127.0.0.1:8000/**

---

## 🎉 You're Ready!

### What You See:
- 🏠 **Homepage** - Beautiful card grid of recipes
- ➕ **"+ Add Recipe"** button - Click to create your first recipe
- 🔍 **Search bar** - Find recipes instantly
- 🎛️ **Filters** - Filter by category and difficulty

---

## 📝 Add Your First Recipe (2 minutes)

### Click "+ Add Recipe" and fill in:

**Basic Info:**
- Title: `Chocolate Chip Cookies`
- Description: `Classic homemade cookies`
- Prep Time: `15` minutes
- Cook Time: `12` minutes
- Servings: `24`
- Difficulty: `Easy`

**Ingredients:**
| Name | Quantity | Unit |
|------|----------|------|
| Flour | 2 | cups |
| Sugar | 1 | cup |
| Chocolate chips | 2 | cups |

**Instructions:**
```
1. Preheat oven to 375°F
2. Mix dry ingredients in a bowl
3. Add wet ingredients and mix well
4. Fold in chocolate chips
5. Bake for 12 minutes until golden
```

**Categories:** Check `Dessert` and `Quick & Easy`

**Click "Create Recipe"** → Done! 🎉

---

## 🎯 What's Next?

### Explore Features:
- ✅ View your recipe (click on the card)
- ✅ Edit recipe (click "Edit Recipe")
- ✅ Search recipes (use search bar)
- ✅ Filter by category (use dropdowns)
- ✅ Add photos (edit recipe → upload image)

### Try the Admin Panel:
1. Go to: **http://127.0.0.1:8000/admin/**
2. Login with your admin credentials
3. See powerful backend interface

### Add More Recipes:
- Breakfast favorites
- Lunch ideas
- Dinner recipes
- Desserts

---

## 📊 Daily Usage

**Start your day:**
```bash
python manage.py runserver
```

**Open browser:**
http://127.0.0.1:8000/

**Start cooking!** 🍳

---

## 🆘 Quick Troubleshooting

### Server won't start?
```bash
# Check Python version
python --version  # Should be 3.11+

# Re-run setup
./.claude/hooks/session-start.sh

# Try different port
python manage.py runserver 8001
```

### Forgot admin password?
```bash
python manage.py createsuperuser
# Create a new admin account
```

### Need to reset?
```bash
rm db.sqlite3
python manage.py migrate
python manage.py setup_recipes
python manage.py createsuperuser
```

---

## 📚 Learn More

- **Complete Workflow**: See `WORKFLOW.md`
- **Development Guide**: See `DEVELOPMENT.md`
- **User Manual**: See `RECIPE_README.md`
- **Technical Details**: See `.claude/skills/django-recipe-app.md`

---

## ✨ Key Features You Have

✅ **Modern UI/UX** - Beautiful glassmorphism design
✅ **Full CRUD** - Create, Read, Update, Delete recipes
✅ **Search & Filter** - Find recipes instantly
✅ **Image Upload** - Add photos to recipes
✅ **Categories** - Organize by type (Dessert, Italian, etc.)
✅ **Responsive** - Works on mobile and desktop
✅ **Admin Panel** - Powerful backend interface
✅ **Tested** - 11 unit tests, all passing
✅ **Production Ready** - Deploy anytime

---

**Happy Cooking! 🍳**

Your recipe app is ready to store all your favorite recipes in one beautiful, organized place.

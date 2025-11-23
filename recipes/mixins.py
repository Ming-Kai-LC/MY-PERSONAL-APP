"""
View mixins for recipe app.
Follows Django best practices for reusable view logic.
"""
from django.contrib import messages
from django.views.generic.edit import ModelFormMixin


class SuccessMessageMixin(ModelFormMixin):
    """
    Mixin to add success message on form save.
    """
    success_message = ""

    def get_success_message(self, cleaned_data):
        """Get the success message."""
        return self.success_message % cleaned_data if self.success_message else ""

    def form_valid(self, form):
        """Add success message when form is valid."""
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response


class TitleMixin:
    """
    Mixin to add page title to context.
    """
    page_title = ""

    def get_page_title(self):
        """Get the page title."""
        return self.page_title

    def get_context_data(self, **kwargs):
        """Add page title to context."""
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        return context


class CategoryContextMixin:
    """
    Mixin to add categories to context for filtering.
    """
    def get_context_data(self, **kwargs):
        """Add categories to context."""
        from .models import Category
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        return context

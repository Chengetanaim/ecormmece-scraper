from .models import Category


categories = Category.objects.all()


def add_variable_to_context(request):
    return {
        'categories': categories
    }
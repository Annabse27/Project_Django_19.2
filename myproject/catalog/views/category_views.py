from django.views.generic import ListView
from catalog.models import Category, Product
from django.core.cache import cache

class CategoryListView(ListView):
    """
    Представление для отображения списка категорий.
    """
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.all()
            cache.set('categories', categories, timeout=60*15)  # Кешируем список категорий на 15 минут
        return categories


class ProductByCategoryListView(ListView):
    """
    Представление для отображения продуктов в выбранной категории.
    """
    model = Product
    template_name = 'catalog/product_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Product.objects.filter(category_id=category_id)

from django.core.cache import cache
from catalog.models import Category, Product


def get_cached_categories():
    """
    Возвращает список категорий с кешированием на 15 минут.
    """
    categories = cache.get('categories')
    if not categories:
        categories = list(Category.objects.all())
        cache.set('categories', categories, 900)  # Кешируем на 15 минут
    return categories


def get_cached_products():
    """
    Возвращает список продуктов с кешированием на 15 минут.
    """
    products = cache.get('products')
    if not products:
        products = list(Product.objects.select_related('owner').all())
        cache.set('products', products, 900)  # Кешируем на 15 минут
    return products


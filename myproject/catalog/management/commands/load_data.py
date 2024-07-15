import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка категорий из фикстур
        with open('catalog/fixtures/catalog_data.json') as file:
            data = json.load(file)
            for item in data:
                if item['model'] == 'catalog.category':
                    Category.objects.create(
                        id=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description']
                    )
                elif item['model'] == 'catalog.product':
                    Product.objects.create(
                        id=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description'],
                        image=item['fields']['image'],
                        category=Category.objects.get(id=item['fields']['category']),
                        price=item['fields']['price'],
                        created_at=item['fields']['created_at'],
                        updated_at=item['fields']['updated_at']
                    )

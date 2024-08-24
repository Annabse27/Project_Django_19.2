from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product


class Command(BaseCommand):
    help = 'Create Moderator group with specific permissions'

    def handle(self, *args, **kwargs):
        # Создание группы
        group, created = Group.objects.get_or_create(name='Модераторы')

        if created:
            self.stdout.write(self.style.SUCCESS('Group "Модераторы" created successfully'))

            # Назначение прав
            permissions = [
                'change_product',  # Право изменять продукт
                'delete_product',  # Право удалять продукт
                'change_category',  # Право изменять категорию продукта
                'publish_product',  # Право публиковать продукт
            ]
            for perm in permissions:
                permission = Permission.objects.get(codename=perm)
                group.permissions.add(permission)

            self.stdout.write(self.style.SUCCESS('Permissions assigned to "Модераторы" group'))
        else:
            self.stdout.write(self.style.WARNING('Group "Модераторы" already exists'))

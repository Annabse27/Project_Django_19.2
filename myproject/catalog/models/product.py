from django.db import models
from django.conf import settings


class Category(models.Model):
    """
    Категория продукта, содержащая наименование и описание.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель продукта, содержащая основные характеристики продукта и привязку к категории.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)  # Поле для публикации


    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_change_category", "Может изменять категорию продукта"),
            ("can_publish_product", "Может публиковать продукт"),
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]



class Version(models.Model):
    """
    Версия продукта с указанием номера и названия версии, а также флага текущей версии.
    """
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE)
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=100)
    is_current = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.product.name} - {self.version_name} ({self.version_number})"

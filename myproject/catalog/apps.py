from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """
    Конфигурация приложения 'catalog'.
    Устанавливает настройки по умолчанию для модели и загружает сигналы при старте приложения.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    def ready(self):
        """
        Импортирует сигналы при готовности приложения.
        """
        import catalog.signals  # файл существует?

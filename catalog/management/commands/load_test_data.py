from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json
import os

class Command(BaseCommand):
    help = 'Загружает тестовые категории и продукты из фикстур'

    def handle(self, *args, **kwargs):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Путь к папке fixtures
        fixture_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'fixtures')

        # Загружаем категории с фиксированными PK
        with open(os.path.join(fixture_dir, 'categories.json'), 'r', encoding='utf-8') as f:
            categories = json.load(f)
            for item in categories:
                Category.objects.create(id=item['pk'], **item['fields'])

        # Загружаем продукты
        with open(os.path.join(fixture_dir, 'products.json'), 'r', encoding='utf-8') as f:
            products = json.load(f)
            for item in products:
                fields = item['fields']
                category_pk = fields.pop('category')
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(category=category, **fields)

        self.stdout.write(self.style.SUCCESS('Данные загружены успешно!'))

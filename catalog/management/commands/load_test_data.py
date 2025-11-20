from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json
import os

class Command(BaseCommand):
    help = 'Загружает тестовые категории и продукты из фикстур'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        fixture_dir = os.path.join(base_dir, '../../fixtures')

        for filename in ['categories.json', 'products.json']:
            with open(os.path.join(fixture_dir, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    model = item['model'].split('.')[1]
                    fields = item['fields']
                    if model == 'category':
                        Category.objects.create(**fields)
                    elif model == 'product':
                        category = Category.objects.get(pk=fields.pop('category'))
                        Product.objects.create(category=category, **fields)

        self.stdout.write(self.style.SUCCESS('Данные загружены успешно!'))

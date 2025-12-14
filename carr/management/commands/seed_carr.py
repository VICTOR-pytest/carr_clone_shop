from django.core.management.base import BaseCommand
import random
from datetime import datetime

from carr.models import carr as CarrModel

BRANDS = [
    'Toyota', 'Honda', 'Volkswagen', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia',
    'Peugeot', 'Renault', 'BMW', 'Mercedes', 'Audi', 'Fiat', 'Jeep'
]

MODELS = [
    'Sedan', 'Hatch', 'Civic', 'Corolla', 'Gol', 'Uno', 'Palio', 'Focus', 'Fusion',
    'Kicks', 'Tucson', 'Sportage', 'Qashqai', 'A3', 'A4', 'Jetta', 'Tiguan', 'Camry'
]

class Command(BaseCommand):
    help = 'Popula o banco com dados falsos de carros (sem dependências externas)'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Número de carros a criar')

    def handle(self, *args, **options):
        count = options['count']
        created = 0
        for i in range(count):
            name = random.choice(BRANDS)
            model = random.choice(MODELS)
            year = random.randint(1995, datetime.now().year)
            # gerar preço entre 10.000 e 300.000 com duas casas decimais
            price = round(random.uniform(10000.0, 300000.0), 2)

            obj = CarrModel.objects.create(name=name, model=model, year=year, price=price)
            created += 1
            self.stdout.write(self.style.SUCCESS(f'Criado: {obj}'))

        self.stdout.write(self.style.SUCCESS(f'Concluído: {created} carros criados.'))

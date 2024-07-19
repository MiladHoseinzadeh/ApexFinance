import random
from django.core.management.base import BaseCommand

from faker import Faker

from finance.models import User, Category, Transaction


class Command(BaseCommand):
	help = "Generates transactions for testing"

	def handle(self, *args, **options):
		fake = Faker()

		categories_list = [
			"Bills",
			"Food",
			"Clothing",
			"Medical",
			"Housing",
			"Salary",
			"Social",
			"Transport",
			"Vacation",
		]
		
		for category in categories_list:
			Category.objects.get_or_create(name=category)

		user = User.objects.filter(username="admin").first()
		if not user:
			user = User.objects.create_superuser(username="admin", password="test")

		categories = Category.objects.all()

		types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]

		for ta in range(20):
			Transaction.objects.create(
				category=random.choice(categories),
				user=user,
				amount=random.uniform(1, 2500),
				date=fake.date_between(start_date="-1y", end_date="today"),
				type=random.choice(types)
			)
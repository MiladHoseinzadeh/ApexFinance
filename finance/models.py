from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	pass


class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


class Transaction(models.Model):
	TRANSACTION_TYPE_CHOICES = (
		("i", "Income"),
		("e", "Expense"),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
	type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.type} of {self.amount} on {self.date} by {self.user}"
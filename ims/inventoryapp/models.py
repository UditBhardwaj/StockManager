import datetime
from django.db import models
from django.utils import timezone

category_choice = (
		('Grocery', 'Grocery'),
		('Stationary', 'Stationary'),
		('Electronics', 'Electronics'),
	)

# Create your models here.
class Stock(models.Model):
	category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice)
	price = models.IntegerField(blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	# issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	# issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.item_name


class Sales(models.Model):
	# name = models.CharField(max_length=50, blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0',blank=True, null=True)
	phone_number = models.IntegerField(default='0', blank=True, null=True)
	total_price = models.CharField(max_length=50, blank=True, null=True)
	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)
	price_per_product = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.issue_by
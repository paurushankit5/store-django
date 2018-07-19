from django.db import models

# Create your models here.
class Category(models.Model):
	cat_name = models.CharField(max_length=255)
	cat_slug = models.CharField(max_length=255, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Subcategory(models.Model):
	subcat_name = models.CharField(max_length=255)
	subcat_slug = models.CharField(max_length=255, unique=True)
	cat_id      = models.ForeignKey(Category, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Subcategory2(models.Model):
	subcat2_name = models.CharField(max_length=255)
	subcat2_slug = models.CharField(max_length=255, unique=True)
	subcat_id      = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

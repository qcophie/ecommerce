import uuid
from utilities import constants
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	
	class Meta:
		ordering = ('name',)
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return f'/{self.id}/'


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to=constants.generate_image_upload_prefix, blank=True, null=True)
	thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ('-date_added',)
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return f'/{self.category.id}/{self.id}/'
	
	def get_image(self):
		if self.image:
			return self.image.url
		return ''
	
	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.image:
				self.thumbnail = self.make_thumbnail(self.image)
				self.save()
				
				return self.thumbnail.url
			else:
				return ''
	
	def make_thumbnail(self, image, size=(300, 200)):
		img = Image.open(image)
		img.convert('RGB')
		img.thumbnail(size)
		
		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality=85)
		
		thumbnail = File(thumb_io, name=image.name)
		
		return thumbnail

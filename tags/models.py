from django.db import models
from django.db.models.signals import pre_save,post_save
from product1.utils import unique_slug_generator
from django.urls import reverse
from product1.models import product



class Tag(models.Model):
	title      = models.CharField(max_length=120)
	slug       = models.SlugField()
	timestamp  = models.DateTimeField(auto_now_add=True)
	active     = models.BooleanField(default=True)
	products   = models.ManyToManyField(product, blank = True)

	def __str__(self):
		return self.title





def tag_pre_save_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
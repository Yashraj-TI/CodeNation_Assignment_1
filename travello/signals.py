import imp
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from . models import Category,Restaurant,Review

@receiver(post_save,sender = Review)
def at_end_update(sender,instance,created,**kwargs):
    if created:
        pass

@receiver(post_save,sender = Restaurant)
def at_end_update(sender,instance,created,**kwargs):
    if created:
        pass




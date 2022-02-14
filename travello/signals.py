import imp
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from . models import Category,Restaurant,Review
from django.core.exceptions import ValidationError

@receiver(pre_save,sender = Review)
def raise_error(sender,instance,**kwargs):
    val = instance.Stars
    if(val<1 or val>5):
        raise ValidationError("Stars should be between 1 to 5")

@receiver(post_save,sender = Review)
def at_end_update(sender,instance,created,**kwargs):
    if created:
        res_name = instance.Restaurant_Id
        count1 = 0
        count2 = 0
        #print("res_name is ")
        #print(res_name)
        r = Review.objects.all()
        for r in r.iterator():
            if(r.Restaurant_Id==res_name):
                count1 += 1
                count2 += r.Stars
        #print("count is ")
        #print(count)
        c = Restaurant.objects.all()
        for c in c.iterator():
            if(c.id==res_name):
                #print("sucess")
                c.Stars = count2//count1
                c.save()

@receiver(post_save,sender = Restaurant)
def at_end_update(sender,instance,created,**kwargs):
    if created:
        res_name = instance.Category
        count = 0
        #print("res_name is ")
        #print(res_name)
        r = Restaurant.objects.all()
        for r in r.iterator():
            if(r.Category==res_name):
                count += 1
        #print("count is ")
        #print(count)
        c = Category.objects.all()
        for c in c.iterator():
            if(c.Name==res_name):
                #print("sucess")
                c.Num_of_Buisness = count
                c.save()
            



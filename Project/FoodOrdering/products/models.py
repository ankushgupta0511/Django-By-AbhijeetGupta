from django.db import models
import uuid

# Create your models here.

# DRY  :- Do not repeat yourself

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)

    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)
    
    class Meta:     # ab BaseModel will be created as a class 
        abstract = True



# class Product(models.Model):
class Product(BaseModel):   # we use inheritance here
    # uid = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    product_name =  models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)



class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    product_measuring = models.CharField(max_length=100,null=True,blank=True ,choices=(('KG','KG'), ('ML','ML'), ('L','L'), (None,None)))
    product_quantity = models.CharField(null=True, blank=True)
    is_quantity = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField()
    
    

    # created_at = models.DateField(auto_created=True)
    # updated_at = models.DateField(auto_created=True)
    
    
    
# class ProductImage(models.Model):
class ProductImage(BaseModel):      # we use inheritance here
    # uid = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_images = models.ImageField(upload_to='products') 
    
    # created_at = models.DateField(auto_created=True)
    # updated_at = models.DateField(auto_created=True)
    



# class DummyModel(models.Model):
class DummyModel(BaseModel):    # we use inheritance here
    pass    
    
    # uid = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)

    # created_at = models.DateField(auto_created=True)
    # updated_at = models.DateField(auto_created=True)



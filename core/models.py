from django.db import models
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.

CATEGORY_CHOICES = (
    ('E','Electronics'),
    ('F','Fashions'),
    ('J', 'jewellery'),
)

LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D', 'danger'),
)




class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
   
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:product", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug": self.slug})
    
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={"slug": self.slug})
    
    
    
  
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f"{self.quantity} of {self.item.title}"
    
    def get_item_price(self):
        return self.quantity * self.item.price
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    
    def get_amount_saved(self):
        return self.get_item_price() - self.get_total_discount_item_price()
    
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    
    
    def __str__(self) -> str:
        return self.user.username
    


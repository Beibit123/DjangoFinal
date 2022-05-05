from django.db import models
from picklefield.fields import PickledObjectField

class ModelManager(models.Manager):
    def only_available(self):
        return self.get_queryset().filter(available = True)
    
    def only_not_available(self):
        return self.get_queryset().filter(available = False)
    
    def price_is_1000(self):
        return self.get_queryset().filter(price = 1000)
    
    def price_is_500(self):
        return self.get_queryset().filter(price = 500)
    
    
class Category(models.Model):
    name = models.CharField('category', max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField('name', max_length = 50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField('description', max_length=300)
    price = models.FloatField("price")
    image = models.CharField('image', max_length=300)
    url = models.CharField('url', max_length=300)
    available = models.BooleanField(default=True)
    
    objects = models.Manager()
    custom_manager = ModelManager()
    
    class Meta:
        abstract = True
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'url': self.url,
            'available': self.available
        }
    
class Salad(Food):
    def __str__(self):
        return self.name
    
class Soup(Food):
    def __str__(self):
        return self.name
    
class Dessert(Food):
    def __str__(self):
        return self.name
    
class Snack(Food):
    def __str__(self):
        return self.name


class Order(models.Model):
    food_id = models.IntegerField()
    user_id = models.IntegerField()
    food_category = models.CharField('category', max_length=300, default="salad")
    
    def __str__(self):
        return self.food_category

    def to_json(self):
        return {
            'id': self.id,
            'food_id': self.food_id,
            'user_id': self.user_id,
            'category': self.food_category,
        }
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator   


class User(AbstractUser): 
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100,unique=True)
    
class Category(models.Model):
    # options=(
    #     ("chocolate cake","chocolate cake"),
    #     ("cheesecake","cheesecake"),
    #     ("cupcake","cupcake"),
    #     ("wedding cake","wedding cake"),
    #     ("birthday cake","birthday cake"),
    #     ("fruit cake","fruit cake"),
    # )
    # caketype=models.CharField(max_length=100,choices=options,default="fruit cake")

    caketype=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)
    
    
    def _str_(self):
        return self.type
    
class Cakes(models.Model):
    
    name=models.CharField(max_length=200,)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class CakeVarients(models.Model):
    price=models.PositiveIntegerField()
    options=(
        ("250g","250g"),
        ("500g","500g"),
        ("1kg","1kg"),
        ("1.5kg","1.5kg"),
        ("2kg","2kg")
    )
    weight=models.CharField(max_length=100,choices=options,default="1kg")
    # cake_message=models.CharField(max_length=200)
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
   
class Offer(models.Model):
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()
    
class Cart(models.Model):
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)
    
class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=100,choices=options,default="order-placed")
    ordered_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)
    
    
class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinLengthValidator(1),MaxLengthValidator(5)])
    comment=models.CharField(max_length=200)




from io import BytesIO
from django.db import models
from django.core.files import File
from PIL import Image
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()

    class Meta:
        ordering=['name']

    def __str__(self) -> str:
        return self.name   

    def get_absolute_url(self):
        return f'/{self.slug}/'     

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug=models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    def avg_rating(self):
        rating=Rating.objects.filter(product=self)
        sum=0 
        for x in rating :
         sum+=x.stars
         if len(rating)==0 :
            return 0
         else :  
            return sum/len(rating) 


    def num_rating(self):
        rating=Rating.objects.filter(product=self)
        return len(rating)    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
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


class Comment(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    comments=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)





class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
